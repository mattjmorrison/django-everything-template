
# Repo Info
set :application, 'django-everything-template'
set :scm, :git
set :repository, 'https://github.com/mattjmorrison/django-everything-template.git'

# Server Info
role :web, "root@localhost"
set :password, 'test'
set :port, 2222
set :deploy_to, "/var/www/django-everything/"

# App Info
set :django_env, 'production'

# Need name of deployed wsgi file
# Need name of deployed settings file
# Need name of optional maintenance wsgi file
# Need server restart command

# Need flag to run syncdb (with and without migrations)
# Need flag to run collect static (with -i *.coffee -i *.less)
# Need flag to run compress
