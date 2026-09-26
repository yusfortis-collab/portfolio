from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<slug:project_slug>/', views.project_detail, name='project_detail'),
]