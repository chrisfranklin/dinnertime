==================
Installation
==================

Pre-Requisites
===============

* `setuptools <http://pypi.python.org/pypi/setuptools>`_
* `virtualenv <http://pypi.python.org/pypi/virtualenv>`_

To install all of these system dependencies on a Debian-based system, run::

	sudo apt-get install python-setuptools
	sudo easy_install virtualenv


Creating the Virtual Environment
================================

First, create a clean base environment using virtualenv::

    virtualenv dinnertime
    cd dinnertime
    source bin/activate


Installing the Project
======================

Install the requirements and the project source::

    sudo apt-get install python-memcache
    python manage.py startapp accounts
	cd path/to/your/dinnertime/repository
    pip install -r requirements.pip
    pip install -e .

Customize the Project
=====================
You should change the UserProfile model in the Accounts application.


Configuring a Local Environment
===============================

If you're just checking the project out locally, you can copy some example
configuration files to get started quickly::

    cp dinnertime/settings/local.py.example dinnertime/settings/local.py
    manage.py syncdb --migrate


Building Documentation
======================

Documentation is available in ``docs`` and can be built into a number of 
formats using `Sphinx <http://pypi.python.org/pypi/Sphinx>`_. To get started::

    pip install Sphinx
    cd docs
    make html

This creates the documentation in HTML format at ``docs/_build/html``.
