from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import StudentForm
from .models import Student


def home(request):
    name = request.GET.get("name")

    if name == "Midhun":
        context = {"name": "Hello Midhun"}
    else:
        context = {"name": name}

    return render("", "app/home.html", context)


class settings(View):
    def get(self, request):
        return render("settings/", "app/settings.html")


class AddStudent(View):

    def get(self, request):
        form = StudentForm()
        context = {"form": form}
        return render(request, "app/add_student.html", context)

    def post(self, request):
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("student_list")
        else:
            return HttpResponse("Failed")


def students_list(request):
    students = Student.objects.all()
    context = {"students": students}

    return render(request, "app/list_students.html", context)


def delete_student(request, id):
    student = Student.objects.get(pk=id)
    student.delete()

    return redirect("student_list")


def edit_student(request, id):
    student = Student.objects.get(pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
        else:
            return HttpResponse("Failed")

    form = StudentForm(instance=student)
    context = {"form": form}
    return render(request, "app/edit_student.html", context)
