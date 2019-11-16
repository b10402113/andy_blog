
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'blog'

urlpatterns = [
    path('', views.index,name = 'blog_index'),
    path('<int:blog_id>', views.detail, name='blog_detail'),
]
