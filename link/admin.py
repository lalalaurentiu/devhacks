from django.contrib import admin
from .models import Doctor, Patient, exercise, TypeOfExercise
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(exercise)
admin.site.register(TypeOfExercise)
