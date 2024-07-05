from django.db import models


class Person(models.Model):
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER)
    profile_picture = models.ImageField(upload_to='profiles/')
    address = models.TextField()
    city = models.CharField(max_length=50)
