# Install

Step 1: Install Docker Engine: 

```shell
# https://docs.docker.com/engine/install/ubuntu/
$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Step 2: Install Docker Compose



```shell
# Manager Docker as a none-root user
# See https://docs.docker.com/compose/install/ for more details
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker

sudo curl -L "https://github.com/docker/compose/releases/download/1.28.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

