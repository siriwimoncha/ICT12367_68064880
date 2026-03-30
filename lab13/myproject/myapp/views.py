from django.shortcuts import render, redirect, get_object_or_404
from .models import Person

from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from django.db.models import Q   # 👈 สำคัญ

def about(request):
    return render(request, 'about.html')

def index(request):
    persons = Person.objects.all()

    # รับค่าค้นหา
    query = request.GET.get('q')

    # ถ้ามีการค้นหา
    if query:
        persons = persons.filter(
            Q(firstname__icontains=query) |
            Q(lastname__icontains=query) |
            Q(nickname__icontains=query) |
            Q(age__icontains=query)
        )

    return render(request, 'index.html', {
        'persons': persons
    })

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