from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from posts.models import Post, Comment
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(
            post=get_object_or_404(Post, pk=self.kwargs['post_id']),
            author=self.request.user
        )
