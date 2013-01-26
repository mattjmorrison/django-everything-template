
node["postgresql"]["databases"].each do |db|

  bash "create_database" do
    user "root"
    code "sudo -u postgres createdb -O #{db['owner']} #{db['name']}"
    not_if "sudo -u postgres psql -l | grep #{db['name']}"
  end

end
