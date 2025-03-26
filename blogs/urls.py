from django.urls import path
from .views import home_page, blog_detail

urlpatterns = [
    path('', home_page, name='home_page'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
]
