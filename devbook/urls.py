from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('userprofile/<int:pk>/edit', views.user_profile_edit, name="user_profile_edit"),
    path('post_url/',views.post_body,name='post_body'),
    path('post_comment/<int:pk>/comments/new',views.post_comment,name='post_comment'),
    path('like_post/<int:pk>/likes/new',views.like_post,name='like_post'),
    path('friends/', views.profile, name='friends'),
    path('post/<int:pk>/edit', views.post_edit, name="post_edit"),
    path('post/<int:pk>/delete', views.post_delete, name="post_delete"),
    path('comment/<int:pk>/edit', views.comment_edit, name="comment_edit"),
    path('comment/<int:pk>/delete', views.delete_comment, name="delete_comment"),
    path('profile/<int:pk>/view', views.user_prof, name='user_prof'),
    path('search/',views.search,name='search'),
    path('inbox/<int:pk>/message',views.get_mail,name='inbox'),
    path('inbox/<int:pk>/createmail',views.mail,name='mail'),
    path('inbox/<int:pk>/send',views.send_mail,name='send_mail'),
    path('inbox/<int:pk>/delete',views.delete_mail,name='delete_mail'),
    path('inbox/<int:pk>/reply',views.reply_mail,name='reply_mail'),
    path('news',views.news,name='news')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
