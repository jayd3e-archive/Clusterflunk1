import os
import base64
import unittest
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Models
from clusterflunk.models.base import Base
from clusterflunk.models.auth import AuthUser
from clusterflunk.models.auth import AuthGroup
from clusterflunk.models.auth import AuthUserGroup
from clusterflunk.models.users import User
from clusterflunk.models.study_groups import StudyGroup
from clusterflunk.models.networks import Network
from clusterflunk.models.categories import Category
from clusterflunk.models.categories import PostCategory
from clusterflunk.models.articles import Article
from clusterflunk.models.article_history import ArticleHistory
from clusterflunk.models.article_comments import ArticleComment
from clusterflunk.models.posts import Post
from clusterflunk.models.post_comments import PostComment
from clusterflunk.models.post_history import PostHistory
from clusterflunk.models.solutions import Solution
from clusterflunk.models.solution_comments import SolutionComment
from clusterflunk.models.solution_history import SolutionHistory
from clusterflunk.models.problems import Problem
from clusterflunk.models.problem_comments import ProblemComment
from clusterflunk.models.problem_history import ProblemHistory
from clusterflunk.models.comments import Comment
from clusterflunk.models.comment_history import CommentHistory
from clusterflunk.models.statuses import Status
from clusterflunk.models.moderators import Moderator
from clusterflunk.models.subscriptions import Subscription

class TestModels(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite://')
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
    
    def testArticles(self):
        session = self.Session()
        
        article = Article(id=1,
                          author_id=1)
        article_rev1 = ArticleHistory(revision=1,
                                      created=datetime.now(),
                                      author_id=1,
                                      body="This is a helpful article.")
        article_rev2 = ArticleHistory(revision=2,
                                      created=datetime.now(),
                                      author_id=2,
                                      body="This is another helpful article.")
        article_rev3 = ArticleHistory(revision=3,
                                      created=datetime.now(),
                                      author_id=3,
                                      body="This is the last helpful article.")
        for ar in [article_rev1, article_rev2, article_rev3]:
            article.history.append(ar)
        session.add(article)
        
        comment = Comment(id=1,
                          author_id=1)
        comment1 = Comment(id=2,
                           author_id=2)
        comment2 = Comment(id=3,
                           author_id=1)
        for c in [comment, comment1, comment2]:
            session.add(c)
        
        article_comment = ArticleComment(article_id=1,
                                         comment_id=1)
        article_comment1 = ArticleComment(article_id=1,
                                          comment_id=2)
        article_comment2 = ArticleComment(article_id=1,
                                          comment_id=3)
        for ac in [article_comment, article_comment1, article_comment2]:
            session.add(ac)
        
        session.flush()
        self.assertTrue(str(article).startswith('<Article'),
                        msg="str(Article) must start with '<Article'")
        self.assertEqual(article.history, [article_rev1, article_rev2, article_rev3])
        self.assertEqual(article_rev1.article, article)
        self.assertEqual(article_rev2.article, article)
        self.assertEqual(article_rev3.article, article)
        self.assertEqual(article.comments, [comment, comment1, comment2])
        self.assertEqual(comment.articles, [article])
        self.assertEqual(comment1.articles, [article])
        self.assertEqual(comment2.articles, [article])

    def testArticleComments(self):
        session = self.Session()

        article = Article(id=1,
                          author_id=1)
        comment = Comment(id=1,
                          author_id=1)
        article_comment = ArticleComment(article_id=1,
                                         comment_id=1)
        session.add(article)
        session.add(comment)
        session.add(article_comment)

        session.flush()
        self.assertTrue(str(article_comment).startswith('<ArticleComment'),
                        msg="str(ArticleComment) must start with '<ArticleComment'")
        self.assertEqual(article_comment.article, article)
        self.assertEqual(article_comment.comment, comment)
        self.assertIn(article_comment, comment.article_comments)
        self.assertIn(article_comment, article.article_comments)
    
    def testArticleHistory(self):
        session = self.Session()

        article_rev = ArticleHistory(revision=1,
                                     created=datetime.now(),
                                     author_id=1,
                                     body="This is a helpful article.")
        session.add(article_rev)
        session.flush()
        self.assertTrue(str(article_rev).startswith('<ArticleHistory'),
                        msg="str(ArticleHistory) must start with '<ArticleHistory'")
    
    def testPosts(self):
        session = self.Session()
        
        post = Post(id=1,
                    author_id=1,
                    study_group_id=1)
        
        problem = Problem(id=1,
                          post_id=1)
        post.problems.append(problem)

        post_rev1 = PostHistory(revision=1,
                                created=datetime.now(),
                                author_id=1,
                                description="This is an assignment.")
        post_rev2 = PostHistory(revision=2,
                                created=datetime.now(),
                                author_id=2,
                                description="This is another assignment.")
        post_rev3 = PostHistory(revision=3,
                                created=datetime.now(),
                                author_id=3,
                                description="This is the last assignment.")
        for p in [post_rev1, post_rev2, post_rev3]:
            post.history.append(p)
        session.add(post)
        
        comment = Comment(id=1,
                          author_id=1)
        comment1 = Comment(id=2,
                           author_id=2)
        comment2 = Comment(id=3,
                           author_id=1)
        for c in [comment, comment1, comment2]:
            session.add(c)
        
        post_comment = PostComment(post_id=1,
                                   comment_id=1)
        post_comment1 = PostComment(post_id=1,
                                    comment_id=2)
        post_comment2 = PostComment(post_id=1,
                                    comment_id=3)
        for pc in [post_comment, post_comment1, post_comment2]:
            session.add(pc)

        category = Category(id=1,
                            name='Test')
        session.add(category)

        post_category = PostCategory(id=1,
                                     post_id=1,
                                     category_id=1)
        post.post_categories.append(post_category)
        
        session.flush()
        self.assertTrue(str(post).startswith('<Post'),
                        msg="str(Post) must start with '<Post'")
        self.assertIn(problem, post.problems)
        self.assertEqual(post, problem.post)
        self.assertEqual(post.history, [post_rev1, post_rev2, post_rev3])
        self.assertEqual(post_rev1.post, post)
        self.assertEqual(post_rev2.post, post)
        self.assertEqual(post_rev3.post, post)
        self.assertEqual(post.comments, [comment, comment1, comment2])
        self.assertEqual(comment.posts, [post])
        self.assertEqual(comment1.posts, [post])
        self.assertEqual(comment2.posts, [post])
        self.assertIn(category, post.categories)
    
    def testPostComments(self):
        session = self.Session()

        post = Post(id=1,
                    author_id=1,
                    study_group_id=1)
        comment = Comment(id=1,
                          author_id=1)
        post_comment = PostComment(post_id=1,
                                   comment_id=1)
        session.add(post)
        session.add(comment)
        session.add(post_comment)

        session.flush()
        self.assertTrue(str(post_comment).startswith('<PostComment'),
                        msg="str(PostComment) must start with '<PostComment'")
        self.assertEqual(post_comment.post, post)
        self.assertEqual(post_comment.comment, comment)
        self.assertIn(post_comment, comment.post_comments)
        self.assertIn(post_comment, post.post_comments)
    
    def testPostHistory(self):
        session = self.Session()

        post_rev = PostHistory(revision=1,
                               created=datetime.now(),
                               author_id=1,
                               name="Awesome Assignment",
                               description="This is a helpful article.",
                               due=datetime.now(),
                               active=datetime.now())
        session.add(post_rev)
        session.flush()
        self.assertTrue(str(post_rev).startswith('<PostHistory'),
                        msg="str(PostHistory) must start with '<PostHistory'")

    def testProblems(self):
        session = self.Session()
        
        problem = Problem(id=1,
                          post_id=1)
        
        solution = Solution(id=1,
                           problem_id=1,
                           author_id=1)
        problem.solutions.append(solution)

        problem_rev1 = ProblemHistory(revision=1,
                                      created=datetime.now(),
                                      author_id=1,
                                      body="This is an assignment.")
        problem_rev2 = ProblemHistory(revision=2,
                                      created=datetime.now(),
                                      author_id=2,
                                      body="This is another assignment.")
        problem_rev3 = ProblemHistory(revision=3,
                                      created=datetime.now(),
                                      author_id=3,
                                      body="This is the last assignment.")
        for p in [problem_rev1, problem_rev2, problem_rev3]:
            problem.history.append(p)
        session.add(problem)
        
        comment = Comment(id=1,
                          author_id=1)
        comment1 = Comment(id=2,
                           author_id=2)
        comment2 = Comment(id=3,
                           author_id=1)
        for c in [comment, comment1, comment2]:
            session.add(c)
        
        problem_comment = ProblemComment(problem_id=1,
                                         comment_id=1)
        problem_comment1 = ProblemComment(problem_id=1,
                                          comment_id=2)
        problem_comment2 = ProblemComment(problem_id=1,
                                          comment_id=3)
        for pc in [problem_comment, problem_comment1, problem_comment2]:
            session.add(pc)

        session.flush()
        self.assertTrue(str(problem).startswith('<Problem'),
                        msg="str(Problem) must start with '<Problem'")
        self.assertIn(solution, problem.solutions)
        self.assertEqual(problem, solution.problem)
        self.assertEqual(problem.history, [problem_rev1, problem_rev2, problem_rev3])
        self.assertEqual(problem_rev1.problem, problem)
        self.assertEqual(problem_rev2.problem, problem)
        self.assertEqual(problem_rev3.problem, problem)
        self.assertEqual(problem.comments, [comment, comment1, comment2])
        self.assertEqual(comment.problems, [problem])
        self.assertEqual(comment1.problems, [problem])
        self.assertEqual(comment2.problems, [problem])
    
    def testProblemComments(self):
        session = self.Session()

        problem = Problem(id=1,
                          post_id=1)
        comment = Comment(id=1,
                          author_id=1)
        problem_comment = ProblemComment(problem_id=1,
                                         comment_id=1)
        session.add(problem)
        session.add(comment)
        session.add(problem_comment)

        session.flush()
        self.assertTrue(str(problem_comment).startswith('<ProblemComment'),
                        msg="str(ProblemComment) must start with '<ProblemComment'")
        self.assertEqual(problem_comment.problem, problem)
        self.assertEqual(problem_comment.comment, comment)
        self.assertIn(problem_comment, comment.problem_comments)
        self.assertIn(problem_comment, problem.problem_comments)

    def testProblemHistory(self):
        session = self.Session()

        problem_rev = ProblemHistory(revision=1,
                                     created=datetime.now(),
                                     author_id=1,
                                     body="This is a problem to be solved.")
        session.add(problem_rev)
        session.flush()
        self.assertTrue(str(problem_rev).startswith('<ProblemHistory'),
                        msg="str(ProblemHistory) must start with '<ProblemHistory'")

    def testSolutions(self):
        session = self.Session()
        
        solution = Solution(id=1,
                            problem_id=1,
                            author_id=1)
        solution_rev1 = SolutionHistory(revision=1,
                                        created=datetime.now(),
                                        author_id=1,
                                        body="This is a helpful solution.")
        solution_rev2 = SolutionHistory(revision=2,
                                        created=datetime.now(),
                                        author_id=2,
                                        body="This is another helpful solution.")
        solution_rev3 = SolutionHistory(revision=3,
                                        created=datetime.now(),
                                        author_id=3,
                                        body="This is the last helpful solution.")
        for sr in [solution_rev1, solution_rev2, solution_rev3]:
            solution.history.append(sr)
        session.add(solution)
        
        comment = Comment(id=1,
                          author_id=1)
        comment1 = Comment(id=2,
                           author_id=2)
        comment2 = Comment(id=3,
                           author_id=1)
        for c in [comment, comment1, comment2]:
            session.add(c)
        
        solution_comment = SolutionComment(solution_id=1,
                                           comment_id=1)
        solution_comment1 = SolutionComment(solution_id=1,
                                            comment_id=2)
        solution_comment2 = SolutionComment(solution_id=1,
                                            comment_id=3)
        for sc in [solution_comment, solution_comment1, solution_comment2]:
            session.add(sc)
        
        session.flush()
        self.assertTrue(str(solution).startswith('<Solution'),
                        msg="str(Solution) must start with '<Solution'")
        self.assertEqual(solution.history, [solution_rev1, solution_rev2, solution_rev3])
        self.assertEqual(solution_rev1.solution, solution)
        self.assertEqual(solution_rev2.solution, solution)
        self.assertEqual(solution_rev3.solution, solution)
        self.assertEqual(solution.comments, [comment, comment1, comment2])
        self.assertEqual(comment.solutions, [solution])
        self.assertEqual(comment1.solutions, [solution])
        self.assertEqual(comment2.solutions, [solution])
    
    def testSolutionsComments(self):
        session = self.Session()

        solution = Solution(id=1,
                            problem_id=1,
                            author_id=1)
        comment = Comment(id=1,
                          author_id=1)
        solution_comment = SolutionComment(solution_id=1,
                                           comment_id=1)
        session.add(solution)
        session.add(comment)
        session.add(solution_comment)

        session.flush()
        self.assertTrue(str(solution_comment).startswith('<SolutionComment'),
                        msg="str(SolutionComment) must start with '<SolutionComment'")
        self.assertEqual(solution_comment.solution, solution)
        self.assertEqual(solution_comment.comment, comment)
        self.assertIn(solution_comment, comment.solution_comments)
        self.assertIn(solution_comment, solution.solution_comments)
    
    def testSolutionHistory(self):
        session = self.Session()

        solution_rev = SolutionHistory(revision=1,
                                       created=datetime.now(),
                                       author_id=1,
                                       body="This is a solution to a problem.")
        session.add(solution_rev)
        session.flush()
        self.assertTrue(str(solution_rev).startswith('<SolutionHistory'),
                        msg="str(SolutionHistory) must start with '<SolutionHistory'")

    def testComments(self):
        session = self.Session()

        comment = Comment(id=1)

        comment_rev1 = CommentHistory(id=1,
                                      revision=1,
                                      created=datetime.now(),
                                      author_id=1,
                                      comment_id=1,
                                      body="U Suk!")
        comment_rev2 = CommentHistory(id=2,
                                      revision=2,
                                      created=datetime.now(),
                                      author_id=1,
                                      comment_id=1,
                                      body="U Suk More!")
        comment_rev3 = CommentHistory(id=3,
                                      revision=3,
                                      created=datetime.now(),
                                      author_id=1,
                                      comment_id=1,
                                      body="U Suk Even More!")
        for cr in [comment_rev1, comment_rev2, comment_rev3]:
            comment.history.append(cr)
        
        session.add(comment)

        session.flush()
        self.assertTrue(str(comment).startswith('<Comment'),
                        msg="str(Comment) must start with '<Comment'")
        self.assertEqual(comment, comment_rev1.comment)
        self.assertEqual(comment, comment_rev2.comment)
        self.assertEqual(comment, comment_rev3.comment)
        self.assertEqual(comment.history, [comment_rev1, comment_rev2, comment_rev3])
    
    def testCommentHistory(self):
        session = self.Session()

        comment_rev = CommentHistory(id=1,
                                     revision=1,
                                     created=datetime.now(),
                                     author_id=1,
                                     comment_id=1,
                                     body="U Suk!")
        session.add(comment_rev)
        session.flush()
        self.assertTrue(str(comment_rev).startswith('<CommentHistory'),
                        msg="str(CommentHistory) must start with '<CommentHistory'")

    def testAuth(self):
        session = self.Session()

        auth_user = AuthUser(id=1,
                             username='jayd3e',
                             password='secret')
        auth_group = AuthGroup(id=1,
                               name='admin')
        auth_user_group = AuthUserGroup(auth_user_id=1,
                                        auth_group_id=1)

        session.add(auth_user)
        session.add(auth_group)
        session.add(auth_user_group)

        session.flush()
        self.assertTrue(str(auth_user).startswith('<AuthUser'),
                        msg="str(AuthUser) must start with '<AuthUser'")
        self.assertTrue(str(auth_group).startswith('<AuthGroup'),
                        msg="str(AuthGroup) must start with '<AuthGroup'")
        self.assertTrue(str(auth_user_group).startswith('<AuthUserGroup'),
                        msg="str(AuthUserGroup) must start with '<AuthUserGroup'")
        self.assertIn(auth_user, auth_group.auth_users)
        self.assertIn(auth_group, auth_user.auth_groups)
        self.assertEqual(auth_user_group.auth_user, auth_user)
        self.assertEqual(auth_user_group.auth_group, auth_group)
    
    def testCategories(self):
        session = self.Session()

        category = Category(id=1,
                            name='Test')
        post_category = PostCategory(id=1,
                                     category_id=1)
        
        post_category.category = category
        session.add(post_category)

        session.flush()
        self.assertTrue(str(category).startswith('<Category'),
                        msg="str(Category) must start with '<Category'")
        self.assertTrue(str(post_category).startswith('<PostCategory'),
                        msg="str(PostCategory) must start with '<PostCategory'")
        self.assertEqual(post_category.category, category)
    
    def testModerators(self):
        session = self.Session()

        study_group = StudyGroup(id=1,
                                 name="Physics 101",
                                 created=datetime.now(),
                                 edited=datetime.now())
        
        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())

        moderator = Moderator(user_id=1,
                              study_group_id=1)
        
        session.add(study_group)
        session.add(user)
        session.add(moderator)

        session.flush()
        self.assertTrue(str(moderator).startswith('<Moderator'),
                        msg="str(Moderator) must start with '<Moderator'")
        self.assertIn(user, study_group.moderators)
        self.assertIn(study_group, user.moderated_groups)
        self.assertEqual(moderator.user, user)
        self.assertEqual(moderator.study_group, study_group)
    
    def testNetworks(self):
        session = self.Session()

        network = Network(id=1,
                          name="Uni of Iowa",
                          created=datetime.now())
        session.add(network)

        study_group1 = StudyGroup(id=1,
                                  name="Class of Physics",
                                  network_id=1)
        study_group2 = StudyGroup(id=2,
                                  name="Class of Math",
                                  network_id=1)
        study_group3 = StudyGroup(id=3,
                                  name="Small Study Group",
                                  network_id=1)
        for sg in [study_group1, study_group2, study_group3]:
            session.add(sg)
        
        session.flush()
        self.assertTrue(str(network).startswith('<Network'),
                        msg="str(Network) must start with '<Network'")
        self.assertEqual(network.study_groups, [study_group1, study_group2, study_group3])
        self.assertEqual(network, study_group1.network)
        self.assertEqual(network, study_group2.network)
        self.assertEqual(network, study_group3.network)

    
    def testStatuses(self):
        session = self.Session()

        status = Status(id=1,
                        created=datetime.now(),
                        body="I luv studying <3",
                        author_id=1)
        
        session.add(status)
        self.assertTrue(str(status).startswith('<Status'),
                        msg="str(Status) must start with '<Status'")
    
    def testStudyGroups(self):
        session = self.Session()

        study_group = StudyGroup(id=1,
                                 name="My cool group",
                                 created=datetime.now(),
                                 edited=datetime.now())
        post = Post(id=1,
                    author_id=1,
                    study_group_id=1)
        study_group.posts.append(post)
        
        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        session.add(user)

        moderator = Moderator(user_id=1,
                              study_group_id=1)
        study_group.moderator.append(moderator)

        session.add(study_group)
        session.flush()
        self.assertTrue(str(study_group).startswith('<StudyGroup'),
                        msg="str(StudyGroup) must start with '<StudyGroup'")
        self.assertIn(post, study_group.posts)
        self.assertEqual(post.study_group, study_group)
        self.assertIn(user, study_group.moderators)
        self.assertIn(study_group, user.moderated_groups)
    
    def testSubscriptions(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        study_group = StudyGroup(id=1,
                                 name="My cool group",
                                 created=datetime.now(),
                                 edited=datetime.now())
        subscription = Subscription(user_id=1,
                                    study_group_id=1)
        
        session.add(study_group)
        session.add(user)
        session.add(subscription)

        session.flush()
        self.assertTrue(str(subscription).startswith('<Subscription'),
                        msg="str(Subscription) must start with '<Subscription'")
        self.assertIn(study_group, user.subscriptions)
        self.assertIn(user, study_group.subscribers)
    
    def testUsers(self):
        pass

    def testWorkingOn(self):
        pass

    