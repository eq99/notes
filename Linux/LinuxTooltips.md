# Tools for linux

## git

```sh
git config --global user.email "youremail@email.com" user.name "yourname"
# bueatiful git lg
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

## zsh

```sh
# zsh & oh-my-zsh:
# For Chines user, please use gitee instead
sudo apt-get install zsh
sh -c "$(wget -O- https://gitee.com/pocmon/ohmyzsh/raw/master/tools/install.sh)"
```

## vim

```sh
# space vim
# https://spacevim.org/quick-start-guide/#linux-and-macos
wget -v https://spacevim.org/install.sh | bash
```

## python

It is very convinient to use python with **conda**.

```sh
# install conda
# https://docs.conda.io/en/latest/miniconda.html#linux-installers
$ wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh
$ chmod +x Miniconda3-py37_4.9.2-Linux-x86_64.sh
$ ./Miniconda3-py37_4.9.2-Linux-x86_64.sh
$ python -V
```

Usages:

```sh
conda create -n <env-name> python=3.7 #! create a new env named learn with python=3.7
conda activate <env-name>             #! using learn
conda remove -n <env-name> --all 	  # delete the whole env
conda init zsh						  # init zsh
conda list                     		  # lits all packages of current env
conda install requests         		  # install requests for current env
conda remove requests          		  # remove requests for current env
conda update requests      		      # update requests
conda env export > environment.yaml   # export env file
conda env create -f environment.yaml  # create env from file
```



# node.js

```shell
# https://github.com/nodesource/distributions/blob/master/README.md#debinstall
# Using Ubuntu
curl -fsSL https://deb.nodesource.com/setup_15.x | sudo -E bash -
sudo apt-get install -y nodejs

# https://registry.npmjs.org
npm config set registry https://registry.npm.taobao.org
npm config get registry
```





# C++

```sh
$ sudo apt install build-essential
$ g++ --version
```



## Screen Shot

```sh
# https://flameshot.org/getting-started/
$ sudo apt install flameshot

```



# obs-studio

```sh
# https://obsproject.com/download
sudo apt install ffmpeg
sudo apt install obs-studio
```



# Gnome Theme

```sh
# https://www.fossmint.com/best-ubuntu-themes/
# https://www.gnome-look.org/p/1099856/
```



# 免密登录服务器

```shell
# @localhost
ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.1.100 # remote ip

# remove with:
ssh-keygen -f "/home/<user>/.ssh/known_hosts" -R "192.168.1.100"
```



# 文件拷贝

```shell
$ scp -r /home/administrator/test/ root@192.168.1.100:/root/
```



# 解压

```shell
tar -xvJf ***.tar.xz
tar -xvzf ***.tar.gz 
```

# 后台运行



```shell
screen -dmS <name>
screen -list
screen -r <name>
screen -S 23536 -X quit
```







