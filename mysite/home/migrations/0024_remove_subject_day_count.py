# Generated by Django 5.0.2 on 2024-04-04 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_subject_day_remove_subject_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='day_count',
        ),
    ]
