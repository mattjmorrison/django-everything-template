********
Database
********

Database Migrations
===================

        A database migration is a script that can be run to apply changes (schema or data)
        to the database. South_ is a Python library that provides database migrations for
        Django.
        
        To initially set up a Django app to have database migrations use the following command::

                ./manage.py <env> schemamigration <app> --init
        

        To automatically generate a database migration based on changes made to model class use 
        the following command::
        
                ./manage.py <env> schemamigration <app> --auto

        To run all database migrations use the following command::

                ./manage.py <env> syncdb --migrate


.. _South: http://south.aeracode.org/
