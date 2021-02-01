# conda

Conda is a manager of your python virtual environment. I like conda because we can chose different python version control.

## Install

```sh
$ wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh
$ chmod +x Miniconda3-py37_4.9.2-Linux-x86_64.sh
$ ./Miniconda3-py37_4.9.2-Linux-x86_64.sh

# Do not install conda in this way:
$ sh -c "$(curl -SfL https://repo.anaconda.com/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh)"
```

## Mirror

This Step is optional.

[清华镜像源地址](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

- Copy the following lines to`.condarc`：

> Note: Windows user should run `conda config --set show_channel_urls yes` to generrate `.condarc`

```yaml
channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

Or You can add a link in this way:

```sh
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
```

You may clean the cache like this:

```sh
$ conda clean -i
```



## Usage

```sh
activate                       # goto base
conda create -n learn python=3.7 # create a new env named learn with python=3.7
conda env list                 # list all envs
conda remove -n learn --all  # delete the whole env
activate learn                 # using learn
conda list                     # lits all packages of current env
conda install requests         # install requests for current env
conda remove requests          # remove requests for current env
conda update requests          # update requests
conda env export > environment.yaml # export and save your env
conda env create -f environment.yaml # create an env from file
```

> Note: You may set your conda path like this: `C:\Users\Alex\anaconda3\Scripts` 
>

You may  install package like this:

```sh
$ pip install <pkg-name> -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

# Flask RESTful API

We will use flask to build RESTful api.

## App

```python
# run.py
from flask import Flask
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class UserAPI(Resource):
    def get(self, id):
        return f'hello, {id}'

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')

if __name__=="__main__":
  app.run(debug=True, port=80, host='0.0.0.0')
```

## Deploy

We will use `uwsgi` to deploy our app. This server's performance is not the best, but it's simple.

> Note: uwsgi won't work on windows.

```sh
$ pip install uwsgi
```

Create the `uwsgi.ini`:

```ini
[uwsgi]
wsgi-file = run.py
callable = app

master = true
processes = 4
enable-threads = True
threads = 20


http=0.0.0.0:80
```

Test your app:

```sh
$ uwsgi --ini uwsgi.ini
$ curl localhost/users/42
# hello, 42
```

## Deploy with docker

> Note: You should run `pip freeze >requirements.txt` to generate `requirements.txt`

```dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["uwsgi", "--ini", "uwsgi.ini"]
```

```sh
# build docker image
$ docker build -t <image-name>:<tag> .
# run
$ docker run -itd --name <container-name> -p 80:80 <image-name>:<tag>

$ docker stop <container-name> # stop
$ docker rm <container-name> # rm
```



