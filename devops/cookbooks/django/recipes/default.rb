
web_app "django" do
  template "django.conf.erb"
  root_dir "/var/www/django-everything/current"
  server_name "django"
  server_aliases "django.localhost"
  http_processes 2
  http_threads 4
end
