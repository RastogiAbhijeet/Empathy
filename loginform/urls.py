from django.conf.urls import url
from . import views

app_name='loginform'

urlpatterns= [
    url(r'^$', views.login, name='login'),
    url(r'validate$', views.validate, name='validate'),
    url(r'signup$', views.signup, name='signup'),
    url(r'create_user$', views.dbentry, name = 'dbentry')
]