from django.conf.urls import url,include
from .views import upload,subset,grouping



urlpatterns = [

    
    url(r'^upload/$',upload),
    url(r'^(?P<filename>.*)/api1/$',subset),
    url(r'^(?P<filename>.*)/api2/$',grouping),

]
