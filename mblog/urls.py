from django.contrib import admin
from django.urls import path
from mblog import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('show/', views.show, name='show'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comment/write/', views.comment_write, name='comment_write'),
    path('<int:board_pk>/comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'), 
] 