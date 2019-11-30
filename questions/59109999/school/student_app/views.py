from django.shortcuts import render
from . import forms, models


# Create your views here.
def student(request):
    student_form = forms.StudentForm(instance=models.Student.objects.first())
    return render(request, 'student_app/add_student.html', {'form': student_form})
