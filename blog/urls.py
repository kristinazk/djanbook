from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    BlogAbout,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
                    )

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<str:username> ', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-post'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', BlogAbout.as_view(), name='blog-about')
]
