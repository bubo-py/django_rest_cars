from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('cars/', views.CarList.as_view(), name='cars-list'),
    path('cars/<int:pk>/', views.CarDetail.as_view(), name='car-detail'),
    path('', views.api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)
