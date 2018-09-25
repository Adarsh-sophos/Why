from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('logout/' , views.logout_user , name = "logout"),
	path('dashboard/' , views.dashboard , name = 'dashboard'),
	path('register/' , views.register , name = 'register'),
	path('', views.index , name = 'index'),
]