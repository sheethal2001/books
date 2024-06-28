from django.urls import path
from .import api_views
from . import views

urlpatterns = [
    path('',views.blog_list,name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('new/', views.add_blog, name='add_blog'),
    path('<int:pk>/edit/', views.update_blog, name='update_blog'),
    path('<int:pk>/delete/', views.delete_blog, name='delete_blog'),

    path('api/blogs/', api_views.BlogListCreateAPIView.as_view(), name='api_blog_list_create'),
    path('api/blogs/<int:pk>/', api_views.BlogRetrieveUpdateDestroyAPIView.as_view(), name='api_blog_detail'),

    
]