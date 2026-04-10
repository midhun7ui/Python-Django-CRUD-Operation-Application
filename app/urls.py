from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("settings/", views.settings.as_view(), name="settings"),
    path("add-student/", views.AddStudent.as_view(), name="add_student"),
    path("student-list/", views.students_list, name="student_list"),
    path("delete-student/<int:id>", views.delete_student, name="delete_student"),
    path("edit-student/<int:id>", views.edit_student, name="edit_student"),
]
