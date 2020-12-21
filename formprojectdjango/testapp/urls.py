from django.conf.urls import url,include
from testapp import views 
from .views import studentregisterview
urlpatterns = [
    url(r'^$',studentregisterview, name = ''),
     
]