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
        pass
    
    def testArticleHistory(self):
        pass
    
    def testAuthUser(self):
        pass
    
    def testAuthGroup(self):
        pass
    
    def testAuthUserGroup(self):
        pass
    
    def testCategories(self):
        pass
    
    def testComments(self):
        pass
    
    def testCommentHistory(self):
        pass
    
    def testModerators(self):
        pass
    
    def testNetworks(self):
        pass
    
    def testPosts(self):
        pass
    
    def testPostComments(self):
        pass
    
    def testPostHistory(self):
        pass
    
    def testPosts(self):
        pass
    
    def testProblems(self):
        pass
    
    def testProblemComments(self):
        pass

    def testProblemHistory(self):
        pass
    
    def testProblems(self):
        pass
    
    def testSolutions(self):
        pass
    
    def testSolutionsComments(self):
        pass
    
    def testSolutionHistory(self):
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

    