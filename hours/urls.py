from django.urls import path
from .views import CategoryView, HoursView, CategoryStatisticsView

app_name = 'hours'

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('hours/', HoursView.as_view(), name='hours'),
    path('category_statistics/', CategoryStatisticsView.as_view(), name='statistics')
]
