from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name ='index'),
    path('apps/', views.applicants, name = 'apps'),
    path('college-history/', views.college_history, name = 'college-history'),
]
