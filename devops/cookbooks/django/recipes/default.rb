
web_app "django" do
  template "django.conf.erb"
  root_dir "/var/www/django-everything/current"
  server_name "django"
  server_aliases "django.localhost"
  http_processes 2
  http_threads 4
end

template '/etc/default/celeryd' do
  source 'celeryd.conf.erb'
  owner 'root'
  group 'root'
  mode '0700'
end

template '/etc/default/celerybeat' do
  source 'celerybeat.conf.erb'
  owner 'root'
  group 'root'
  mode '0700'
end

template '/etc/init.d/celeryd' do
  source 'celeryd.erb'
  owner 'root'
  group 'root'
  mode '0755'
  variables ({
    :celery_defaults => '/etc/default/celeryd',
  })
end

template '/etc/init.d/celerybeat' do
  source 'celerybeat.erb'
  owner 'root'
  group 'root'
  mode '0755'
end



# celery_app "django" do
#   template "celery.conf.erb"
#   root_dir "/var/www/django-everything/current"
# end
