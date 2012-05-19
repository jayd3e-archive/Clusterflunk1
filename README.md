Proposed Website:
-----------------
I think it's about time that we as a generation change the way we approach school work. The fact of the matter is that
working as a group is often far more efficient than working individually. When you work with other people to solve a
problem, each party brings in a unique point of view, which results in the problem getting solved faster as each party
contributes the knowledge they are most comfortable with. We usually achieve this at the moment by holding study groups
or doing our homework with roommates. This works out well, but there are two reasons why I think we can come up with
something better to get our school work done faster. The first being that study groups are often terribly inefficient
and off task. Who do you normally have study groups with? Your friends. So you inevitably end up talking about other
social aspects of your lives and completely lose site of the fact that you are trying to get your school work done so
you can go and have more of those social experiences. Let's face it, we all want to get done with our school work as
quickly as possible, learn the material, take the test, and go on to actually use that information.  The second reason
I think we can make a better system is that we are not using all of our resources. In a class filled with 300-400 people,
we study/collaborate with probably less than 5% of them(guess statistic but still true). I think this is a huge problem,
because I know there are number of students who are very good in certain areas and wouldn't mind sharing their expertise
with others and in doing so actually learn more themselves(“People retain 90% of what they learn when they teach someone
else/use immediately.” - http://www.psychotactics.com/blog/art-retain-learning/).
 
Everything in today's world is social. At the present, few topics can be completely mastered by one individual, so it's
important that each of us specializes in a specific field and than ask each other for help when we encounter a problem
that is not within the bounds of our knowledge. In addition, very few jobs in the real world are completely independent.
Collaboration in today's world is truly the name of the game. This all stems from the fact that everyone learns at
different rates and has different strengths and weaknesses to bring the table, resulting in a complex web of skill sets.
So it really makes sense that we should adapt this real world model in the way we do our work at school. I also find
that a lot of the work that is done each year is completely wasted when the next generation of students rolls around.
All of the constructive discussions, all of the written work, and the failed tests are just thrown away, never to be
looked at again. Don't you think that the students next year could have used all of that material? Or more importantly,
don't you think that YOU could have used last years material :).
 
All of this speculation about our current methods of completing the age old task of “homework” has motivated me to attempt
to come up with a better system. Very simply put, this site will allow students to “collaborate and discuss their homework.”
Without delving into any specifics, I need help from everyone finding the best ways to accomplish that one simple goal.
This may involve students showing examples, asking questions, explaining complicated topics through articles/guides, posting
test-prep materials and class summaries, uploading resources or linking to other sites.
 
Previous Attempts:
------------------
So I have tried making this site twice now. Both attempts have failed, due to one reason. I didn't do enough planning/design
work before starting the project, and would spend a great deal of time spinning my wheels on what the site was suppose to DO
and HOW it was going to do it. To avoid this problem this time, I decided that it would be a good idea to do a rediculous
amount of planning before starting the project, so that when I get to the point where I start coding it, I will know exactly
how EVERY SINGLE PAGE will function and look.
 
“Ok......where do I come in?”:
------------------------------
I'm making this site for each one of you, and with any luck many more. So this time around, I thought to myself, why not actually
talk to the people the site is going to be for. I need to know what you guys want this site to be and more importantly, what you
want it to do. The first step in this process is coming up with a monolithic list of possible features that the site will have. I
have compiled a list of the features I have in my head right now below. Tell me what you think of the list, and also give me some
suggestions as to what else this site should be able to do. This is just a brainstorming session, so the sky is the limit. I really
want to see how long we can make this list. As people make suggestions, I will update my feature list.
 
Feature List:
-------------
Base Features-
-Store user-specific data, such as names, genders, e-mails, and other profile-related information(limited information).
-Allow users to join a "network" for their specific school or multiple networks if they so choose.
-Allow users to create/delete groups public and private within their network. Groups can represent small study groups, a discussion
group of 10-20 people, or even an entire class, made up of 300-400 people. Private groups can be used to do things like have your
friends proof-read a paper.
-Allow users to add “post” to each group, thus creating a "tide" page. This post could be an assignment, a test, a project, a lab, or any other obligation that
a student might have.
-Each post will have meta-data attached to it, such as the due date of the post.
-Allow users to attach resources to a post. This could be a word document of some kind, a pdf, or an excel file.
-Allow users to propose a "solution" to a post.
-Allow users to comment on every element of the "solution".  This includes the post, the solution, and even specific lines in the solution.
-Allow users to search all posts on every network in all public(not private) groups.
-Allow users to write articles on specific topics. “Articles” are basically for people who may want to write more extensively about a
particular topic to teach to other students. Students will be able to link to various articles from all over the site to explain topics,
thus reducing the amount of times a common topic has to be explained.
-Allow users to comment on articles.
-A feed/timeline to show all of the activity going on in the groups you are subscribed to.

Suggested Features:
-------------------
-A whitelist(friend’s list/blacklist) where people can add people who they want to hear more from, and not see the people they don’t
want to hear from.

Development Schedule:
---------------------
High Level:
5 months for development of two products, the website(clusterflunk.com) and a mobile application(for as many platforms as possible in the timeframe).
3 months for testing/quality assurance of the two deliverable products.
RELEASE DATE: 8/16/12

Low Level:
Database:
Database schema
SQLAlchemy Models
backbone.js models(get information printing for each model) using Gapvis pattern
Caching(possibility, not necessarily something that is important up front)
Pyramid Views:
Every view returns the same file, but provides a different starting point in the app
Frontend
Landing page
Index/Dashboard
Agenda Page(advanced calendar)
Groups Page(add/remove groups from your profile) - Reverse mechanic of Google+ adding groups
Articles Page - Creating/Deleting/Editing your articles.  Featured articles in a group(highest rated ones etc.)
Tide Page
Write library for textareas, that handles all input to the site.  So we can eventually allow users to insert math/science symbols
Testing
Write tests for models
Write tests for view code
Write frontend javascript tests

Stack
-----
Postgresql
Pyramid
Mako
SQLAlchemy
Alembic
Jquery
Jquery-ui
Underscore.js
Backbone.js
Backbone.js-layoutmanager
Require.js or a home-brew module system
handlebars.js (client-side templating)

Mobile App Stack
----------------
Different stylesheet

INSTALL
-------
1. Untar this --> http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.7.tar.gz#md5=dcc105e5a3907a9dcaa978f813a4f526
2. cd into it and type `python setup.py install`.  This will install a console script into your system python to allow you to use virtualenv.
3. Make a directory to keep your Python install in.
4. wget http://www.python.org/ftp/python/2.7/Python-2.7.tgz, and untar it.
5. ./configure, make, make install
6. Go to your projects directory(i.e. ~/Projects) and type `git clone git@github.com:jayd3e/Clusterflunk.git`.
7. Install git.
8. cd into the resulting directory(Clusterflunk) and type `virtualenv --no-site-packages --python=/path/to/Python-2.7/bin/python env`.
9. Then finally type `source env/bin/activate`, and `python setup.py develop`.
10. Run `paster serve development.ini` to start the server.