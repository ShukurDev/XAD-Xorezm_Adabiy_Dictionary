from django.urls import path
from . import views

urlpatterns = [ 
	path('' ,views.salom , name = 'home'),
]