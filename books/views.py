from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    """
    List books or add a book if logged in.
    The perform_create method associates the book with the logged in user.
    """
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        """
        Check for user authentication.
        """
        serializer.save(owner=self.request.user)
    
    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'owner__username',
        'title',
    ]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a book and edit or delete it if you own it.
    """
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Book.objects.annotate()
