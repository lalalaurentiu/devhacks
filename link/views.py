from django.shortcuts import render, HttpResponse
from .models import Doctor, Patient, exercise, TypeOfExercise
from datetime import datetime

app_name = "link"

def home (request, slug, date):

    template_name = "home.html"
    person = Patient.objects.get(slug=slug)
    exercises = exercise.objects.filter(pacient=person, date=date)
    links = exercise.objects.filter(pacient=person)
    
    
    context = {
        "exercises": exercises,
        "links": links,
        "person_slug": slug,
    }

    return render(request, template_name, context)

def calendar(request, slug):
    person = Patient.objects.get(slug=slug)
    exercises = exercise.objects.filter(pacient=person)
    context = {
        "exercises": exercises
    }
    template_name = "calendar.html"
    return render(request, template_name, context)
