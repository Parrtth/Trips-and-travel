# Generated by Django 5.0.2 on 2024-04-04 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='Tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.tour'),
        ),
    ]
