from django.conf.urls import url
from . import views

app_name = 'empathy'

urlpatterns = [
    url(r'^$', views.validate, name='validate'),    
    url(r'^pdf_download/$', views.output_pdf, name='output_pdf'),
    url(r'^register/$', views.register,name="register")
]