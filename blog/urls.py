from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('blogpost/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blogpost/create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blogpost/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('blogpost/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('blogs/', include('blog.urls')),
]