from django.urls import path
from .views import (home,
                    about,
                    PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',home,name="blog-home"),
    path('',PostListView.as_view(),name="blog-home"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('about/', about, name="blog-about"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/',PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

