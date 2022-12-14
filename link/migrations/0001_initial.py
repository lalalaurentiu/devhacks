# Generated by Django 4.1.3 on 2022-11-20 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='exercises')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='link.person')),
                ('specialty', models.CharField(max_length=30)),
            ],
            bases=('link.person',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='link.person')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            bases=('link.person',),
        ),
        migrations.CreateModel(
            name='exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('home', 'Home'), ('doctor', 'Doctor')], default='Home', max_length=9)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('typeofexercise', models.ManyToManyField(related_name='exercises', to='link.typeofexercise')),
                ('pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link.patient')),
            ],
        ),
    ]
