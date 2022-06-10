from django.urls import path
from .views.APIViewDemo import UserListView, UserDetailView

urlpatterns = [
    path('APIViewDemo', UserListView.as_view()),
    path('APIViewDemo/<str:pk>', UserDetailView.as_view()),
]
