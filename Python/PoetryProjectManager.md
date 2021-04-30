# 安装

[Poetry Official Site Here](https://python-poetry.org/docs/)

```sh
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# auto complement Oh-My-Zsh
mkdir $ZSH_CUSTOM/plugins/poetry
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry
```

For `oh-my-zsh`, you must then enable poetry in your `~/.zshrc` plugins, like:

```shell
plugins(git poetry)
```



# 使用方法

```sh
# Example here: https://python-gino.org/docs/zh/1.0/tutorials/fastapi.html#write-a-simple-server
$ poetry add fastapi uvicorn gunicorn
$ poetry add -D pytest requests
$ poetry install
$ poetry run uvicorn gino_fastapi_demo.asgi:app --reload
$ poetry run gunicorn "app:create_app()"
$ poetry run alembic init migrations
$ poetry run alembic revision --autogenerate -m 'add users table'
$ poetry run alembic upgrade head
$ poetry run pytest
```



```sh
poetry config --list
```

