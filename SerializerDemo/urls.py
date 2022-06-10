from django.urls import path
from .views import StudentView
from .views import TeacherView

urlpatterns = [
    path('student/<str:pk>', StudentView.as_view()),
    path('teacher/<str:pk>', TeacherView.as_view()),
]
