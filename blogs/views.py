from rest_framework.views import APIView
from rest_framework import generics , status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 , render ,redirect
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope


from .models import BlogPost, Comment, UpvoteDownvote
from .serializers import BlogPostSerializer, CommentSerializer, UpvoteDownvoteSerializer



class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    template_name = 'blogpost_list.html'
    
    def get(self, request, *args, **kwargs):
        blogposts = self.get_queryset()
        return render(request, self.template_name, {'blogposts': blogposts})
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return redirect('blogpost-list')


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrTokenHasScope]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        comments = Comment.objects.filter(blogpost=instance)
        comments_serializer = CommentSerializer(comments, many=True)
        votes = UpvoteDownvote.objects.filter(blogpost=instance)
        votes_serializer = UpvoteDownvoteSerializer(votes, many=True)
        response_data = {
            'blog_post': serializer.data,
            'comments': comments_serializer.data,
            'votes': votes_serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    
    
    
class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrTokenHasScope]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrTokenHasScope]


class UpvoteDownvoteListView(generics.ListCreateAPIView):
    queryset = UpvoteDownvote.objects.all()
    serializer_class = UpvoteDownvoteSerializer
    permission_classes = [IsAuthenticatedOrTokenHasScope]


class UpvoteDownvoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UpvoteDownvoteSerializer
    permission_classes = [IsAuthenticatedOrTokenHasScope]


