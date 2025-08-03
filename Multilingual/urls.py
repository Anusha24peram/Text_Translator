from django.urls import path
from . import views

urlpatterns = [
    path('', views.detect_view, name='detect_view')
]
