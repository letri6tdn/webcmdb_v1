from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    #path('search/<str:pk>/', views.machine_detail, name='machine_detail'),
    path('search/<str:pk>/edit/', views.machine_edit, name='machine_edit'),
]