from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.list_items),
    path('notes/<int:pk>', views.detail),
]
