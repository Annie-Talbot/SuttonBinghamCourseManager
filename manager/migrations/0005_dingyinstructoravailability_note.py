# Generated by Django 4.0.6 on 2022-08-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_stage_dingyinstructoravailability_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='dingyinstructoravailability',
            name='note',
            field=models.CharField(max_length=255, null=True),
        ),
    ]