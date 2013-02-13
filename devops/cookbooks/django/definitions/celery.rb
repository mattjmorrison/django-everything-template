
define :celery_app do
  celeryd = "celeryd-#{params[:name]}"
  celerybeat = "celerybeat-#{params[:name]}"

  template "/etc/default/#{celeryd}" do
    source 'celeryd.conf.erb'
    owner 'root'
    group 'root'
    mode '0700'
    variables ({
      :chdir => params[:root_dir]
    })
  end

  template "/etc/init.d/#{celeryd}" do
    source 'celeryd.erb'
    owner 'root'
    group 'root'
    mode '0755'
    variables ({
      :celery_defaults => "/etc/default/#{celeryd}",
    })
  end

  template "/etc/default/#{celerybeat}" do
    source 'celerybeat.conf.erb'
    owner 'root'
    group 'root'
    mode '0700'
    variables ({
      :chdir => params[:root_dir]
    })
  end

  template "/etc/init.d/#{celerybeat}" do
    source 'celerybeat.erb'
    owner 'root'
    group 'root'
    mode '0755'
    variables ({
      :celery_defaults => "/etc/default/#{celeryd}",
      :celerybeat_defaults => "/etc/default/#{celerybeat}",
    })
  end

end
