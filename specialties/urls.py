from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='specialties'),
    path('<int:pk>', views.special, name='special'),
]