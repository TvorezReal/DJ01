from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='films_home'),
	path('create_feedback/', views.create_feedback, name='add_feedback')
]