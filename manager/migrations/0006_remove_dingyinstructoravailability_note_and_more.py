# Generated by Django 4.0.6 on 2022-08-20 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_dingyinstructoravailability_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dingyinstructoravailability',
            name='note',
        ),
        migrations.CreateModel(
            name='AssistantInstructorAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned', models.BooleanField()),
                ('assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.assistantinstructor')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.course')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.stage')),
            ],
        ),
    ]
