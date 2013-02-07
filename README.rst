.. 

Dinner Time - Alpha
======================

What is dinner time?
--------------------

We connect people who want to eat together and help them share food. If you would like to see a running version of this code then please head along to http://tablesurf.in

Copyright
---------
Copyright Piemonster Technology Ltd

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Quickstart
----------

To bootstrap the project::

    virtualenv dinnertime
    source dinnertime/bin/activate
    cd path/to/dinnertime/repository
    pip install -r requirements.pip
    pip install -e .
    cp dinnertime/settings/local.py.example dinnertime/settings/local.py
    manage.py syncdb --migrate
    manage.py yummly_meta


News and Updates
----------------

Please head along to http://facebook.com/tablesurfin/ or check out http://tablesurf.in/blog/

Issues
------

Please report any problems you find in the issues section above, if you have code to contribute then even better!

Roadmap
-------

We use Trello to keep track of tasks and progress, please go to https://trello.com/board/tablesurfin/50bc0679c8c6df481400495b to see what we are currently working on.

Testing
-------

You can run the tests with the following command::
	python manage.py test

We also use a Jenkins test server, please go to 

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory. It is also available online at https://tablesurfin.readthedocs.org/en/latest/

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
