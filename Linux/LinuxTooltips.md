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
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## vim

```sh
# space vim
sh -c "$(curl -sLf https://spacevim.org/install.sh)"
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







