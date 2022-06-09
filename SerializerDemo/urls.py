from django.urls import path
from .views import StudentView

urlpatterns = [
    path('student/<str:pk>', StudentView.as_view()),
]
