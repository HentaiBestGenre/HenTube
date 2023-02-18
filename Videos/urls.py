from django.urls import path
from . import views

urlpatterns = [
    path('<int:video_id>/', views.video, name='video'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('set_comment/', views.create_comment, name='set_comment'),
    path('react/', views.react, name='react'),
]

app_name = 'Videos'
