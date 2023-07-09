from django.urls import path
from . import views
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('deleteTask/<int:pk>', views.deleteTask, name='deleteTask'),
    path('', views.index, name='index'),
]
