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
 
All of this speculation about our current methods of completing the age old task of “homework” has motivated me to 
attempt to come up with a better system. Very simply put, this site will allow students to “collaborate and discuss 
their homework.” Without delving into any specifics, I need help from everyone finding the best ways to accomplish that
one simple goal. This may involve students showing examples, asking questions, explaining complicated topics through 
articles/guides, posting test-prep materials and class summaries, uploading resources or linking to other sites.
 
Previous Attempts:
------------------
So I have tried making this site twice now. Both attempts have failed, due to one reason. I didn't do enough
planning/design work before starting the project, and would spend a great deal of time spinning my wheels on what the
site was suppose to DO and HOW it was going to do it. To avoid this problem this time, I decided that it would be a good
idea to do a rediculous amount of planning before starting the project, so that when I get to the point where I start
coding it, I will know exactly how EVERY SINGLE PAGE will function and look.
 
“Ok......where do I come in?”:
------------------------------
I'm making this site for each one of you, and with any luck many more. So this time around, I thought to myself, why not
actually talk to the people the site is going to be for. I need to know what you guys want this site to be and more
importantly, what you want it to do. The first step in this process is coming up with a monolithic list of possible
features that the site will have. I have compiled a list of the features I have in my head right now below. Tell me what
you think of the list, and also give me some suggestions as to what else this site should be able to do. This is just a
brainstorming session, so the sky is the limit. I really want to see how long we can make this list. As people make
suggestions, I will update my feature list.
 
Feature List:
-------------

###Base Features
-  add questions to main feed page.
-  list latest questions from subscribed groups.
-  list latest posts from subscribed groups.
-  add post to subscribed group.
-  list all groups that a user is subscribed to.
-  list groups in network <----- limit 500
-  add a group to a network
-  subscribe to a group
-  unsusbscribe from a group
-  view a profile
-  login/register to site
-  logout of site
-  comment on a post
-  comment on a post's comment
-  comment on a status
-  watch a post
-  vote a comment up or down
-  list watched posts
-  view a group
-  view a post

###Suggested Features:
-  A whitelist(friend’s list/blacklist) where people can add people who they want to hear more from, and not see the people
they don’t want to hear from.
-  Ability to attach a resource to everything.  To a post, comment, article, everything.

Development Schedule:
---------------------
High Level:
5 months for development of two products, the website(clusterflunk.com) and a mobile application(for as many platforms
as possible in the timeframe). 3 months for testing/quality assurance of the two deliverable products.
RELEASE DATE: 8/16/12

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
Clusterflunk uses vagrant to setup a virtualized development environment for working on the site.

1.  Install vagrant per the [getting started](http://vagrantup.com/v1/docs/getting-started/index.html) guide.
2.  Type `mkdir ~/boxes; cd ~/boxes`
3.  Clone the [Clusterstack](https://github.com/Clusterflunk/Clusterstack.git) repo into this directory, and 
cd into the created directory.  IMPORTANT: Create a directory in your home directory called 'webapp'.  The file path
'/opt/webapp' will get mounted to this directory, so you can do all of your development work locally on your own computer.
4.  Run `vagrant box add ubuntu-1110-server-amd64 http://timhuegdon.com/vagrant-boxes/ubuntu-11.10.box`.
5.  Run `vagrant up`.  After this command completes, you can very easily access your new box by typing `vagrant ssh`.
6.  Copy the ssh key pair from your home directory into your shared vagrant directory.  The command should look something
like so `cp -r ~/.ssh ~/boxes/Clusterstack/`.  Then after sshing into your virtual box(`vagrant ssh`), you can than put those
keys into the home directory of your vagrant user, by typing something along the lines of `cp -r /vagrant/.ssh ~/`.
7.  Also add your username and email to git's config, by issueing these two commands: `git config --global user.name "Your Name"
    git config --global user.email you@example.com` with your own personal data substituted in.
8.  Clone the Clusterflunk repo, by issuing this command: `cd /opt/webapp; git clone git@github.com:Clusterflunk/Clusterflunk.git`.
9.  Finally, run the setup script by typing `./setup` in the Clusterflunk directory.