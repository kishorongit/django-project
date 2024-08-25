from django.urls import path, include

from .views import *

urlpatterns = [
    path("", index_view, name="index"),
    path("form", TeacherCreateView.as_view(), name="teacher-form"),
    path("list", TeacherListView.as_view(), name="teacher-list"),
    path("teacher/<int:pk>/", TeacherUpdateView.as_view(), name="teacher-update"),
    path("delete/<int:pk>/", TeacherDeleteView.as_view(), name="teacher-delete"),
]
