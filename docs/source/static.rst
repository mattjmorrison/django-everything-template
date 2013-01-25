************
Static Files
************


Static Files
============


        Typically, static files are not served using Django. Instead, a web server
        like Apache_, Nginx_ or a CDN_ will handle such things. Because each Django
        app can contain it's own static files this makes it difficult because the
        static files are spread across multiple directories. Do not fear, there is 
        a simple solution, Django's static files app.
        
        To collect all static files and copy them to your chosen target location, 
        use the following command::
        
                ./manage.py <env> collectatic --noinput -i *.coffee -i *.less
                
        You may have noticed the ``-i coffee -i less`` flag that I used in that
        example, check out the next section about webassets for more info about 
        that.
        
Django-Compressor
=========

        `Django Compressor`_ makes it possible to pre-compile static files in a number of 
        different ways. The demo Django app demonstrates converting coffeescript
        and less into JavaScript and css respectively and also minifying the 
        generated JavaScript and css. All of the real magic happens in how
        you include the static source files in your html templates. There is a
        command that can go find all of the static files that are referenced 
        in all of your templates and run them through their respective compilers
        and move them to your static files location.
        
        Here is how to run static files through the django-compressor filters::

                ./manage.py <env> compress
                
        The ``-i *.coffee -i *.less`` mentioned above is so that none of your 'raw source' files,
        your CoffeeScript and less files actually get copied to your static folder, these files
        will be sent through the coffee and less compilers to generate JavaScript and CSS then
        that output will be moved to your static root.


.. _Apache: http://httpd.apache.org/
.. _Nginx: http://nginx.org/
.. _CDN: http://en.wikipedia.org/wiki/Content_delivery_network
.. _`Django Compressor`: http://django_compressor.readthedocs.org/en/latest/index.html
