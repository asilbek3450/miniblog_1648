from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<int:id>/', views.blog, name='blog'),
    path('blog/<int:id>/like/', views.like_blog, name='like_blog'),
    path('blog/<int:id>/comment/', views.comment, name='comment'),
    path('blog/<int:id>/comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
]