from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('secondQuiz/', views.secondQuiz, name='secondQuiz'),
    path('result/', views.result, name='result'),
    path('win/', views.win, name='win'),
]
