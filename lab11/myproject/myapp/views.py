from django.shortcuts import render, redirect, get_object_or_404
from .models import Person

# แสดงข้อมูล
def index(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})


# เพิ่มข้อมูล
def form_view(request):
    if request.method == 'POST':
        Person.objects.create(
            firstname=request.POST.get('firstname'),
            lastname=request.POST.get('lastname'),
            nickname=request.POST.get('nickname'),
            age=request.POST.get('age')  # 👈 เพิ่ม
        )
        return redirect('/')

    return render(request, 'form.html')


# แก้ไข
def edit(request, id):
    person = get_object_or_404(Person, id=id)

    if request.method == 'POST':
        person.firstname = request.POST.get('firstname')
        person.lastname = request.POST.get('lastname')
        person.nickname = request.POST.get('nickname')
        person.age = request.POST.get('age')  # 👈 เพิ่ม
        person.save()
        return redirect('/')

    return render(request, 'form.html', {'person': person})


# ลบ
def delete(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect('/')