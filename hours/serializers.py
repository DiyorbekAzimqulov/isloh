from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Category, HoursCategory


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class HoursCategorySerializer(ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = HoursCategory
        fields = [
            'id',
            'category',
            'activity_in_minutes'
        ]


class CategoryStatisticsSerializer(Serializer):
    activity_in_minutes = serializers.IntegerField()
    category__name = serializers.CharField()


class DayCategoryStatisticsSerializer(CategoryStatisticsSerializer):
    day = serializers.DateTimeField()


class WeekCategoryStatisticsSerializer(CategoryStatisticsSerializer):
    week = serializers.DateTimeField()


class MonthCategoryStatisticsSerializer(CategoryStatisticsSerializer):
    month = serializers.DateTimeField()


class YearCategoryStatisticsSerializer(CategoryStatisticsSerializer):
    year = serializers.DateTimeField()
