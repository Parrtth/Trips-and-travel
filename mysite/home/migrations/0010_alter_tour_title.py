# Generated by Django 5.0.2 on 2024-03-31 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='title',
            field=models.CharField(max_length=40, null=True),
        ),
    ]