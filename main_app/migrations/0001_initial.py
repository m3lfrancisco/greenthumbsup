# Generated by Django 4.0.3 on 2022-05-27 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('plant_type', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('sunlight', models.CharField(max_length=100)),
                ('adoption_date', models.DateField(verbose_name='Adoption Date')),
                ('notes', models.TextField(blank=True, max_length=250)),
                ('fertilizers', models.ManyToManyField(blank=True, to='main_app.fertilizer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Watering Date')),
                ('time', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], default='M', max_length=1, verbose_name='Time of Day')),
                ('frequency', models.CharField(max_length=100)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plant')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plant')),
            ],
        ),
    ]
