from django.shortcuts import render,redirect,get_object_or_404
from .models import student

# def home(request):
#     return render(request,'student/student_list.html')

def student_list(request):
    students=student.objects.all()
    return render(request,'student/student_list.html',{'students':students})

def student_form(request):
    return render(request,'student/student_form.html')

def save_student(request):
    if request.method=="POST":
        student_id=request.POST.get('student_id')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        age=request.POST.get('age')
        grade=request.POST.get('grade')
        add=student(student_id=student_id,first_name=first_name,last_name=last_name,age=age,grade=grade)
        add.save()
        return redirect('student-list')

def delete_record(request):
    student.objects.get.delete(student_id=id)
    return render(request,'student/student_list.html')

def Update_record(request,id):
    first_name=request.data.get('first_name')
    last_name=request.data.get('last_name')
    age=request.data.get('age')
    grade=request.data.get('grade')
    student.objects.filter(id=id).update(first_name=first_name,last_name=last_name,age=age,grade=grade)
    return redirect('/')

    

