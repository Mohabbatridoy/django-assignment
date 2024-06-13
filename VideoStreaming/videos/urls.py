from django.urls import path
from .views import video_list, video_detail

urlpatterns = [
    path('', video_list, name='video_list'),
    path('video/<int:pk>/', video_detail, name='video_detail'),
]
