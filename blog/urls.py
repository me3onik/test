from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('title_posts/<str:title>/', views.title_detail, name='detail_title'),
]
