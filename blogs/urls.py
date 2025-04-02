from django.urls import path
from .views import home_page, blog_detail, add_blog

urlpatterns = [
    path('', home_page, name='home_page'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('add_blog', add_blog, name='blog_qoshish')
]
