# Generated by Django 4.0.6 on 2022-08-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssistantInstructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True)),
                ('experience', models.IntegerField(choices=[(0, 'No Experience'), (1, 'Little Experience'), (2, 'Competent'), (3, 'Very Competent')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DingyInstructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True)),
                ('experience', models.IntegerField(choices=[(0, 'No Experience'), (1, 'Little Experience'), (2, 'Competent'), (3, 'Very Competent')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True)),
                ('experience', models.IntegerField(choices=[(0, 'No Experience'), (1, 'Little Experience'), (2, 'Competent'), (3, 'Very Competent')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True)),
                ('start_date', models.DateField()),
                ('assistants', models.ManyToManyField(to='manager.assistantinstructor')),
                ('helpers', models.ManyToManyField(to='manager.helper')),
                ('instructors', models.ManyToManyField(to='manager.dingyinstructor')),
            ],
        ),
    ]
