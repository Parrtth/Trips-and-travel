# Generated by Django 5.0.2 on 2024-04-04 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_remove_subject_day_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='day_count',
            field=models.IntegerField(null=True),
        ),
    ]
