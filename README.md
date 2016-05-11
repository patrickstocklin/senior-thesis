# Mn Contrast Agent Image Processor

To Deploy:

Clone the project from its repository on Github:

```mkdir -p ProjectDirectory```

```cd ProjectDirectory```

```git clone https://github.com/patrickstocklin/SeniorThesis```

Order Vagrant to provision the system:

```vagrant up```

SSH into the system:

```vagrant ssh```

Install libgtk dependencies:

```sudo apt-get -y install libgtk2.0-0```

Install Conda by running the .sh script. Follow the prompted directions:

```sudo bash scripts/Miniconda2-latest-Linux-x86\_64.sh```

Logout of your SSH session and log in again for changes to occur. Create your environment for image-analysis libraries and packages by running the createEnvironment.sh script:

```sudo bash scripts/createEnvironment.sh```

Finally, activate your environment (called Canny):

```source activate Canny```
