.. 

dinnertime
======================

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



Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
