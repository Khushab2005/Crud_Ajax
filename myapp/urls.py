from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',home_page,name='home_page'),
    path('display',display,name='display'),
    path('insert',insert,name='insert'),
    path('deletes',deletes,name='deletes'),
    path('employeid',employeid,name='employeid'),
    path('updates',updates,name='updates'),
]