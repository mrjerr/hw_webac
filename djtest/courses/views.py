from django.shortcuts import render
from django import forms
from .models import Student
# Create your views here.


# class StudentForm(forms.Form):
#     name = forms.CharField()
#     birthdate = forms.DateField()
#     email = forms.EmailField()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

def index(request):
    # form = StudentForm({'name': 'Alex'})
    form = StudentForm()
    return render(request, 'index.html', {'form': form})
