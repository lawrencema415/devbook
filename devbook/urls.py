from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('post_url/',views.post_body,name='post_body'),
    path('post_comment/<int:pk>/comments/new',views.post_comment,name='post_comment'),
    path('like_post/<int:pk>/likes/new',views.like_post,name='like_post'),
    path('friends/', views.profile, name='friends'),
    path('post/<int:pk>/edit', views.post_edit, name="post_edit"),
    path('post/<int:pk>/delete', views.post_delete, name="post_delete"),
    path('comment/<int:pk>/edit', views.comment_edit, name="comment_edit"),
    path('comment/<int:pk>/delete', views.delete_comment, name="delete_comment"),
    path('profile/<int:pk>/view', views.user_prof, name='user_prof')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
