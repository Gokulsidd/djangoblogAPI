from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, CommentListView,CommentDetail, UpvoteDownvoteListView , UpvoteDownvoteDetailView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('blogs/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('comment/', CommentListView.as_view(), name='comment_create'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment_detail'),
    path('vote/', UpvoteDownvoteListView.as_view(), name='vote_create'),
    path('vote/<int:pk>/', UpvoteDownvoteDetailView.as_view(), name='upvotedownvote-detail'),
]
    


