from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('result/', views.ResultView.as_view(), name='result'),
]