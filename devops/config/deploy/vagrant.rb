
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
