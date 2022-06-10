from django.urls import path
# APIViewDemo
from .views.APIViewDemo import UserListView, UserDetailView
# ViewSetDemo
from .views.ViewSetDemo import UserViewSet
# GenericAPIViewDemo
from .views.GenericAPIViewDemo import UsersGenericAPIView, UserGenericAPIView
# GenericViewSetDemo
from .views.GenericViewSetDemo import UserGenericViewSet
# ModelViewSetDemo
from .views.ModelViewSetDemo import UserModelViewSet

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
    path('GenericAPIViewDemo', UsersGenericAPIView.as_view()),
    path('GenericAPIViewDemo/<str:pk>', UserGenericAPIView.as_view()),
    path('GenericViewSetDemo', UserGenericViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('GenericViewSetDemo/<str:pk>', UserGenericViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('UserModelViewSetDemo', UserModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('UserModelViewSetDemo/<str:pk>', UserModelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
]
