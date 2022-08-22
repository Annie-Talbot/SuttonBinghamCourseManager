# Generated by Django 4.0.6 on 2022-08-21 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_rename_assistant_assistantinstructoravailability_staff_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelperAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.course')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.assistantinstructor')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.stage')),
            ],
        ),
    ]