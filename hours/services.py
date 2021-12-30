from django.db.models import Count, Sum
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth, TruncYear

from .models import HoursCategory
from user.models import User


def category_statistics(user: User, trunc: str):
    trunc_type = {
        'day': TruncDay('created_datetime'),
        'week': TruncWeek('created_datetime'),
        'month': TruncMonth('created_datetime'),
        'year': TruncYear('created_datetime')
    }
    if trunc == 'day':
        query = HoursCategory.objects.filter(user=user).annotate(day=trunc_type[trunc])\
            .values('day', 'category__name').annotate(
            activity_in_minutes=Sum('activity_in_minutes')).values('day', 'activity_in_minutes', 'category__name')
        return query
    elif trunc == 'week':
        query = HoursCategory.objects.filter(user=user).annotate(week=trunc_type[trunc]) \
            .values('week', 'category__name').annotate(
            activity_in_minutes=Sum('activity_in_minutes')).values('week', 'activity_in_minutes', 'category__name')
        return query
    elif trunc == 'month':
        query = HoursCategory.objects.filter(user=user).annotate(month=trunc_type[trunc]) \
            .values('month', 'category__name').annotate(
            activity_in_minutes=Sum('activity_in_minutes')).values('month', 'activity_in_minutes', 'category__name')
        return query
    elif trunc == 'year':
        query = HoursCategory.objects.filter(user=user).annotate(year=trunc_type[trunc]) \
            .values('year', 'category__name').annotate(
            activity_in_minutes=Sum('activity_in_minutes')).values('year', 'activity_in_minutes', 'category__name')
        return query
