from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.demo,name='demo')
]
