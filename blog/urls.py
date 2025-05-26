from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post-list-page'),
    path('posts/<slug:slug>/', views.post_detail, name='posts-detail-page'),
    path('autors/', views.autor_list, name='autor_list'),
    path('autors/<int:autor_id>/', views.autor_detail, name='autor_detail'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/<str:slug>/', views.tag_detail, name='tag_detail'),
]