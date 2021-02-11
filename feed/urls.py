from django.urls import path

from .views import (
    feed_list_all,
    feed_list_detail,
    feed_add_view,
    feed_delete_view,
    feed_edit_view
)

app_name = 'feed'
urlpatterns = [
    path('', feed_list_all, name='feed-feed_list_all'),
    path('<int:feed_id>/', feed_list_detail, name='feed_list_detail'),
    path('add/', feed_add_view, name='feed-add'),
    path('<int:feed_id>/delete/', feed_delete_view, name='feed-delete'),
    path('<int:feed_id>/edit/', feed_edit_view, name='feed-edit'),
]
