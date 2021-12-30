from .models import Category, HoursCategory
from .serializers import CategorySerializer, HoursCategorySerializer, \
    DayCategoryStatisticsSerializer, WeekCategoryStatisticsSerializer, MonthCategoryStatisticsSerializer, \
    YearCategoryStatisticsSerializer
from rest_framework import generics
from rest_framework.views import APIView
from .services import category_statistics


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HoursView(generics.ListCreateAPIView):
    serializer_class = HoursCategorySerializer

    def get_queryset(self):
        return HoursCategory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryStatisticsView(generics.ListAPIView):
    """
    statistics about category
    """

    def get_queryset(self):
        trunc = self.request.query_params.get('trunc')
        return category_statistics(user=self.request.user, trunc=trunc)

    def get_serializer_class(self):
        trunc = self.request.query_params.get('trunc')
        if trunc == 'day':
            return DayCategoryStatisticsSerializer
        elif trunc == 'week':
            return WeekCategoryStatisticsSerializer
        elif trunc == 'month':
            return MonthCategoryStatisticsSerializer
        elif trunc == 'year':
            return YearCategoryStatisticsSerializer
