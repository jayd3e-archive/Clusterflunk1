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
from clusterflunk.models.statuses import Status

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
                          body="U Suk!",
                          author_id=1)
        comment1 = Comment(id=2,
                           body="No U Suk!",
                           author_id=2)
        comment2 = Comment(id=3,
                           body="Nope!",
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
                          body="U Suk!",
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
                          body="U Suk!",
                          author_id=1)
        comment1 = Comment(id=2,
                           body="No U Suk!",
                           author_id=2)
        comment2 = Comment(id=3,
                           body="Nope!",
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
        pass
    
    def testPostHistory(self):
        pass

    def testProblems(self):
        pass
    
    def testProblemComments(self):
        pass

    def testProblemHistory(self):
        pass

    def testSolutions(self):
        pass
    
    def testSolutionsComments(self):
        pass
    
    def testSolutionHistory(self):
        pass

    def testComments(self):
        session = self.Session()
    
    def testCommentHistory(self):
        pass

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
        pass
    
    def testNetworks(self):
        pass
    
    def testStatuses(self):
        pass
    
    def testStudyGroups(self):
        pass
    
    def testSubscriptions(self):
        pass
    
    def testUsers(self):
        pass

    def testWorkingOn(self):
        pass

    