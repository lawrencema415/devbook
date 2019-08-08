from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('post_url/',views.post_body,name='post_body'),
    path('post_comment/<int:pk>/comments/new',views.post_comment,name='post_comment')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
