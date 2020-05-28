from django.forms import ModelForm
from django import forms
from .models import Student, Course


#-------------------------------------------Student Form------------------------------------------------------------
class Student_Form(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter First Name.'}),required = True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter Last Name.'}),required = True)
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter Contact No.'}),required = True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter Email Address.'}),required = True)
    course = forms.CharField(widget=forms.Select(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter Course Name.'}),required = True)
    fees = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter Fees *INR.'}),required = True)
    class Meta:
        model = Student
        fields = '__all__'

#-------------------------------------------Course Form------------------------------------------------------------
class Course_Form(forms.ModelForm):
    course = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter Course Name.'}),required = True)
    fees = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter Fees *INR.'}),required = True)
    class Meta:
        model = Course
        fields = '__all__'
