# Generated by Django 5.0.2 on 2024-04-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_tour_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='day',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='night',
            field=models.IntegerField(null=True),
        ),
    ]
