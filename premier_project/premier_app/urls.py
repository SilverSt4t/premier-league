from django.contrib import admin
from django.urls import path
from premier_app import views_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/matches/', views_api.match_data),
    path('api/top_scorers/', views_api.top_scorers),
]