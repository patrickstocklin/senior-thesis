# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|
  
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |v|
    v.name = "Canny-Edge-Detection"
    v.customize ["modifyvm", :id, "--memory", 256]
  end

  config.vm.synced_folder "./images", "/home/vagrant/images"
  config.vm.synced_folder "./scripts", "/home/vagrant/scripts"

  #config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    # vb.gui = true
  #end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get -y install libgtk2.0-0
    wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    touch createEnvironment.sh
    chmod 777 createEnvironment.sh
    echo "cd miniconda2" >> createEnvironment.sh
    echo "conda update conda" >> createEnvironment.sh
    echo "conda create --name Canny biopython" >> createEnvironment.sh
    echo "conda install -c menpo opencv" >> createEnvironment.sh
    echo "conda install --name Canny -c menpo opencv" >> createEnvironment.sh

      #Get library/package sharer or some crap
    #sudo apt-get -y install libgtk2.0-0
      #Install conda
    #sudo bash Miniconda2-latest-Linux-x86_64.sh
      #Set Up Envs
    #sudo bash createEnvironment.sh
      #Activate
    #source activate Canny

  SHELL

end
