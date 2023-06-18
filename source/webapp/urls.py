from django.contrib import admin
from django.urls import path

from webapp.views import cat_name, cat_stats

urlpatterns = [
    path('', cat_name),
    path('cat_stats/', cat_stats)
]
