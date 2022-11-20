from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Doctor(Person):
    specialty = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.specialty

class Patient(Person):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    def save(self):
        self.slug = slugify(self.first_name + " " + self.last_name)
        super(Patient, self).save()

    def get_absolute_url(self):
        return reverse('link:home', args=[self.slug])

class TypeOfExercise(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='exercises', blank=True)
    def __str__(self):
        return self.name



class exercise(models.Model):
    CHOICES =(
    ("home", "Home"),
    ("doctor", "Doctor"),
    )
  
    location = models.CharField(max_length=9,
                  choices=CHOICES,
                  default="Home")
    pacient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    typeofexercise = models.ManyToManyField(TypeOfExercise, related_name='exercises')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    def __str__(self):
        return self.pacient.first_name + " " + self.pacient.last_name

    def get_date(self):
        return self.date.strftime("%Y-%m-%d")
