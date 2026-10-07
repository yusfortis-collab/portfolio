from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<slug:project_slug>/', views.project_detail, name='project_detail'),
    path("internship/", views.internship, name="internship"),
    path("diploma/", views.diploma, name="diploma"),
    path("latin-honor/", views.latin_honor, name="latin_honor"),
]