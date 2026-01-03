from rest_framework import viewsets, generics, status, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from posts.models import Post, Like
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class FeedView(generics.ListAPIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            like.delete()
            return Response(
                {"status": "unliked"},
                status=status.HTTP_204_NO_CONTENT
            )

        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )

        return Response(
            {"status": "liked"},
            status=status.HTTP_201_CREATED
        )
