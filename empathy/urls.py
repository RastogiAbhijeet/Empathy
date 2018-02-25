from django.conf.urls import url
from . import views

app_name = 'empathy'

urlpatterns = [
    url(r'^$', views.validate, name='validate'),    
    url(r'^register/$', views.register,name="register"),
    url(r'^events/$', views.event_register,name="event_register"),
    url(r'^event_profile/$', views.event_push,name="event_push"),
    url(r'^getnames$', views.sendnames, name = 'sendnames'),
    url(r'^shortlist$',views.updateShortList, name = "updateShortList"),
    url(r'^position$', views.updatePositionList, name = 'updatePositionList'),
    url(r'^sendVerification/$', views.sendMail, name="sendMail"),
    url(r'^xls_generation/$', views.reportGeneration, name="reportGeneration"),
    url(r'^loadCsv/$', views.loadCsv, name="loadCsv"),
    url(r'^noticeList/$', views.sendNoticeList, name="sendNoticeList"),
    url(r'^downloadfile/$', views.output_file, name="outputfile"),
    url(r'^certidownload/$', views.certificate_push, name="certificatePush"),
    url(r'^infoDe/$', views.bulkReportGenerationAthleticMeet, name = "bulkReportGenerationAthleticMeet"),
    url(r'^deleteEvent/$', views.deleteEvent, name = "deleteEvent")
    
]