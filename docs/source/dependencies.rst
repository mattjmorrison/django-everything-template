************
Dependencies
************

PIP_ is a great tool for managing dependencies.

Installing Dependencies
=======================

        It is a good practice to keep your dependencies separated by what you need to deploy
        your application and what you need to test your application or run your application
        locally. 

        To install development specific dependencies use the following command::
                
                pip install -r requirements/dev.txt
        
        To install production dependencies use the following command::
        
                pip install -r requirements/base.txt

.. _PIP: http://pypi.python.org/pypi/pip/