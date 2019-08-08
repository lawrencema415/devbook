from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post_url/',views.post_body,name='post_body'),
    path('post_comment/<int:pk>/comments/new',views.post_comment,name='post_comment')
]
