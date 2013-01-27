
desc "Dependency Management"
namespace :deps do

	desc "Install Ruby Dependencies"
	task :ruby do
		system "cd devops && bundle install"
	end

	desc "Install Python Dependencies"
	task :python, :env do |t, args|
		system "pip install -r devops/requirements/#{args[:env]}.txt"
	end

	desc "Install Node Dependencies"
	task :node do
		system "cd devops && npm install"
	end

end

desc "Sphinx Documentation"
namespace :docs do

	desc "build documentation"
	task :build do
		system "sphinx-build -b html docs/source docs/build"
	end

end
