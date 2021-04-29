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
    'app_name.apps.app_nameConfig', # activate the new app
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

In `app_name/views.py`

```python


```

In `app_name/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('api/app_name/', views.LeadListCreate.as_view() ),
]
```


Step 














