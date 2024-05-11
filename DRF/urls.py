from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('gurutugas/', views.GuruTugas_list),
    path('gurutugas/<int:pk>/', views.GuruTugas_detail),
    path('tempat/', views.Tempat.as_view()),
    path('tempat/<int:pk>/', views.TempatDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)