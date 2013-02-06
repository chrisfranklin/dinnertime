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

If you are using virtualenvwrapper (recommended) then::
    
    mkvirtualenv dinnertime
    workon dinnertime


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
Take a look at the settings file in dinnertime/settings/base.py


Configuring a Local Environment
===============================

If you're just checking the project out locally, you can copy some example
configuration files to get started quickly::

    cp dinnertime/settings/local.py.example dinnertime/settings/local.py
    manage.py syncdb --migrate

Populate the Recipe Database
===============================

To download recipes from the yummly API add the correct key to yummly/management/commands/yummly_meta.py and run the following command::

    python manage.py yummly_meta <model> 

Make sure you set <model> to one of "Ingredient, Recipe, Course, Allergy or Diet"


Building Documentation
======================

Documentation is available in ``docs`` and can be built into a number of 
formats using `Sphinx <http://pypi.python.org/pypi/Sphinx>`_. To get started::

    pip install Sphinx
    cd docs
    make html

This creates the documentation in HTML format at ``docs/_build/html``.
