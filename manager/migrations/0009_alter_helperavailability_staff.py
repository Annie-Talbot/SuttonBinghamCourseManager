# Generated by Django 4.0.6 on 2022-08-21 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_helperavailability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helperavailability',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.helper'),
        ),
    ]