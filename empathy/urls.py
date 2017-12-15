from django.conf.urls import url
from . import views

app_name = 'empathy'

urlpatterns = [
    url(r'^$', views.validate, name='validate'),    
]