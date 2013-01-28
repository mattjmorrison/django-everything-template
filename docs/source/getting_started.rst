***************
Getting Started
***************

Before you get started
======================

	You'll need to install:

		#. rvm_ (and ruby >= 1.9)
		#. python_ (>= 2.7 & < 3)
		#. virtualenv_
		#. nodejs_ (>= 0.8)


Get the code
============

	#. Checkout the code from github::

		git clone http://github.com/mattjmorrison/django-everything-template.git --recurse-submodules

	#. Get up in there::

		cd django-everything-template


Setup your Python environment
=============================

	#. Create a virtualenv::

		virtualenv myvirtualenv

	#. Activate the virtualenv::

		source myvirtualenv/bin/activate

	#. Install the development dependencies::

		pip install -r devops/requirements/dev.txt


Setup your Ruby environment
===========================

	#. Create a gemset::

		rvm gemset create mygemset

	#. Activate your gemset::

		rvm use @mygemset

	#. Install the dependencies::

		cd devops && bundle install && cd ..


Setup your Node.js environment
==============================

	#. Install the dependencies::

		cd devops && npm install && cd ..


Run the demo locally
====================

	#. Create a database::

		./manage.py dev syncdb --migrate --noinput

	#. Start the development server::

		./manage.py dev runserver

	#. Navigate to http://localhost:8000/demo/ to see that less
	   and CoffeeScript are working

	#. Navigate to http://localhost:8000/demo/person/ to see the
	   RESTful 'person' resource is working


Create a local virtual production-like server
=============================================

	#. cd into the devops directory::

		cd devops

	#. add a vagrant box (this will take a while)::

		vagrant box add ubuntu-12.04 http://dl.dropbox.com/u/1537815/precise64.box

	#. create a new virtual server (this will also take a while)::

		vagrant up

	#. ssh to the box and set the root password (this is used for the local deploy)::

		vagrant ssh
		sudo -i
		passwd  #enter "test" when prompted


Deploy the project to the virtual production-like server
========================================================

	#. cd into the devops directory::

		cd devops

	#. use capistrano to deploy (this will take a while)::

		cap deploy

	#. Navigate to http://localhost:8080/demo/ to see that less
	   and CoffeeScript are working

	#. Navigate to http://localhost:8080/demo/person/ to see the
	   RESTful 'person' resource is working


.. _rvm: https://rvm.io/
.. _python: http://www.python.org/
.. _virtualenv: http://pypi.python.org/pypi/virtualenv
.. _nodejs: http://nodejs.org/
