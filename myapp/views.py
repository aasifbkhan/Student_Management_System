from django.shortcuts import render, redirect
from .forms import Student_Form, Course_Form
from django.contrib import messages
from .models import Student, Course
# Create your views here.
def index(request):
    return render(request,'index.html')

#------------------------------------------Student_View-----------------------------------------------------------
def student(request):
    student_form = Student_Form(request.POST or None)
    if student_form.is_valid():
        student_form.save()
        messages.success(request, 'Record Inserted Successfully...!!')
        student_form = Student_Form()

    stud = Student.objects.all()
    crs = Course.objects.all()
    n = len(stud)
        
    context = {'student_form':student_form, 'no_of_rows':n, 'range':(n), 'stud':stud, 'crs':crs}

    return render(request, "student.html", context)

def student_update(request, id):
    stud = Student.objects.get(id=id)
    context = {'stud':stud}
    return render(request, "student_update.html", context)

def update(request, id):
    stud = Student.objects.get(id=id)
    Student_form = Student_Form(request.POST, instance = stud)
    if Student_form.is_valid():
        Student_form.save()
        messages.success(request, 'Record Updated Successfully...!!')
        return redirect("/student/")
    context = {'stud':stud}
    return render(request, "student_update.html", context)

def delete(request, id):
     stud = Student.objects.get(id=id)
     stud.delete()
     messages.success(request, 'Record Deleted Successfully...!!')
     return redirect("/student/")

#--------------------------------------------------Course_View---------------------------------------------------
def course(request):
    course_form = Course_Form(request.POST or None)
    if course_form.is_valid():
        course_form.save()
        messages.success(request, 'Record Inserted Successfully...!!')
        course_form = Course_Form()

    crs = Course.objects.all()
    n = len(crs)
    context = {'course_form':course_form, 'no_of_rows':n, 'range':(n), 'crs':crs}
    return render(request, "course.html" , context)

def course_update(request, id):
    crs = Course.objects.get(id=id)
    context = {'crs':crs}
    return render(request, "course_update.html", context)

def update_crs(request, id):
    crs = Course.objects.get(id=id)
    course_form = Course_Form(request.POST, instance = crs)
    if course_form.is_valid():
        messages.success(request, 'Record Updated Successfully...!!')
        course_form.save()
        return redirect("/course/")
    context = {'crs':crs}
    return render(request, "course_update.html", context)

def delete_crs(request, id):
     crs = Course.objects.get(id=id)
     crs.delete()
     messages.success(request, 'Record Deleted Successfully...!!')
     return redirect("/course/")