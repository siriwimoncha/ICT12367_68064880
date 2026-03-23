from django.db import models
from django import forms


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, default="-")
    nickname = models.CharField(max_length=100, default="-")
    age = models.IntegerField(default=0)  # 👈 เพิ่ม
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname
    
nickname = models.CharField(max_length=100)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'nickname']  # 👈 เพิ่ม