# Install

```shell
python -m venv venv
source venv/Script/activate

pip install django djangorestframework

django-admin startproject project_name .

python manage.py runserver
```

# First api

Step 1: start an app

```shell
django-admin startapp app_name
```

Step 2: setting up your app

In  `project_name/settings.py`: 

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name.apps.App_nameConfig', # <---register the new app
]
```

Step 3: setup urls

In `project_name/urls.py`

```python
from django.urls import path, include

urlpatterns = [
    path('', include('app_name.urls')),
]
```

Step 4: Write view functions

In `app_name/views.py`

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello')
```

In `app_name/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.index),
]
```


Step 5: Start server

```shell
python manage.py runserver
```

Step 6: Visit `localhost:8000/hello`


# Database

In `setting.py` :
```python
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '116.62.161.62',
        'PORT': '5432'
    }
}
```









