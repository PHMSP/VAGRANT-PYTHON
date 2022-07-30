Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.box_download_insecure = true
  
  config.disksize.size = "50GB"

  config.vm.network "forwarded_port", guest: 8888, host: 8888 

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 4096
    vb.cpus = 2
    vb.name = "teste_zeppelin"
  end

end