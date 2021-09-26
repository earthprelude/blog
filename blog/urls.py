from django.urls import path 
from .views import (add_comment, comment_approve, comment_remove,
    post_list, post_detail, post_new, post_edit, 
    post_draft_list, post_publish, post_remove)

urlpatterns = [
    path('post/new', post_new, name="post_new"),
    path('drafts/', post_draft_list, name = "post_draft_list"),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/remove/', post_remove, name='post_remove'),
    path('post/<int:pk>/publish/', post_publish, name='post_publish'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('', post_list, name='post_list')
]