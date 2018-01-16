from django.conf.urls import url
from . import views

app_name = 'empathy'

urlpatterns = [
    url(r'^$', views.validate, name='validate'),    
    url(r'^pdf_download/$', views.output_pdf, name='output_pdf'),
    url(r'^register/$', views.register,name="register"),
    url(r'^events/$', views.event_register,name="event_register"),
    url(r'^event_profile/$', views.event_push,name="event_push"),
    url(r'^getnames$', views.sendnames, name = 'sendnames'),
    url(r'^shortlist$',views.updateShortList, name = "updateShortList"),
    url(r'^ruom$',views.updateShortList, name = "updateShortList"),
]