# Generated by Django 5.0.2 on 2024-04-13 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_tour_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date',
        ),
    ]