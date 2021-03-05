from django.urls import path
from . import views

#app_name = affiliate

urlpatterns = [
    path('',views.home,name='home'),
]
