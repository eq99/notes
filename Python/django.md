# Install

```shell
python -m venv venv
source venv/Script/activate

pip install django djangorestframework

django-admin startproject project_name .

python manage.py runserver
```

# First page

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


# Database and first api

https://www.django-rest-framework.org/tutorial/quickstart/


Step 1: Config database.

```shell
pip install psycopg2-binary djangorestframework
```

In `setting.py` :
```python
INSTALLED_APPS = [
    'rest_framework', # <--- add restframework
]

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

Step 2: create superuser

```shell
pyhon manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
```

step 3: create `serializers.py`

```python
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
```

Step 4：Reafact `views.py`

```python
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
```

Step 5: Refactor app's `urls.py`

https://www.django-rest-framework.org/api-guide/routers/

```python
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups',views.GroupViewSet)
urlpatterns = router.urls
```
In `project/urls.py`
```python
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

```






