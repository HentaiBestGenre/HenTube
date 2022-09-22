from django.urls import path
from . import views

urlpatterns = [
    path('<int:channel_id>/', views.channel, name="Channel"),
    path('subscribe/', views.subscribe, name="Subscribe"),
]

app_name = 'Channels'
