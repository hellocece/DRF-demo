# APIViewDemo
from django.urls import path
from .views.APIViewDemo import UserListView, UserDetailView

# ViewSetDemo
from .views.ViewSetDemo import UserViewSet


# 或者这样写
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'ViewSetDemo', UserViewSet)
# urlpatterns = urlpatterns.__add__(router.urls)

urlpatterns = [
    path('APIViewDemo', UserListView.as_view()),
    path('APIViewDemo/<str:pk>', UserDetailView.as_view()),
    path('ViewSetDemo', UserViewSet.as_view({'get': 'list'})),
    path('ViewSetDemo/<str:pk>', UserViewSet.as_view({'get': 'retrieve'})),
]

