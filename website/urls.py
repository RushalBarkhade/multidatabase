from django.urls import path
from website.views import *

urlpatterns = [
    path('read-db/',ReadDBAPI.as_view(),name="read-db"), 
    path('write-db/',WriteDBAPI.as_view(),name="write-db"), 
    ]
  
