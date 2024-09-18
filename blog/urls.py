from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view.as_view(), name='posts_list_view'),
    path('<int:pk>/', views.post_detail_view.as_view(), name='post_detail'),
    path('new/', views.add_new_post.as_view(), name='add_post'),
    path('<int:pk>/update', views.post_update.as_view(), name='update'),
    path('<int:pk>/delete', views.post_delete_view.as_view(), name='delete'),


]
