from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get_queryset(self):
    #     return Category.objects.filter(user=self.request.user)
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
