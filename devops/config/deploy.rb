load 'deploy' if respond_to?(:namespace)

def python
    "#{current_release}/virtualenv/bin/python"
end

def pip
    "#{current_release}/virtualenv/bin/pip"
end

def django(args, flags="")
    run "#{python} #{current_release}/manage.py #{django_env} #{args} #{flags}"
end

after 'deploy:update_code', :setup_python_environment
before :setup_django_environment, :setup_node_environment
after :setup_python_environment, :setup_django_environment
before 'deploy:create_symlink', :setup_database_environment
after 'deploy:update', 'deploy:cleanup'

task :setup_node_environment do
    run "cd #{current_release}/devops && npm install"
end

task :setup_python_environment do
    run "virtualenv #{current_release}/virtualenv"
    run "#{pip} install -r #{current_release}/devops/requirements/base.txt"
end

task :setup_django_environment do
    django("compress")
    django("collectstatic", "-i *.coffee -i *.less --noinput")
    settings_file = django_env.gsub(".", "/")
    run "ln -s #{current_release}/project/settings/#{settings_file}.py #{current_release}/project/settings/deployed.py"
end

task :setup_database_environment do
    django("syncdb", "--noinput --migrate")
end

namespace :deploy do

    task :restart do
        run "sudo apache2ctl graceful"
    end

    task :finalize_update, :except => { :no_release => true } do
        run "chmod -R g+w #{latest_release}" if fetch(:group_writable, true)
    end

end