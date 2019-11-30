from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class_list= [
    ('Class IIX', 'Class IIX'),
    ('Class IX', 'Class IX'),
    ('Class X', 'Class X'),
    ('Class XI', 'Class XI'),
    ('Class XII', 'Class XII')
    ]
    student_class = forms.CharField(label='Class', widget=forms.Select(choices=class_list,attrs={'style': 'width:175px'}))
    class Meta:
        model = models.Student
        fields = '__all__'
