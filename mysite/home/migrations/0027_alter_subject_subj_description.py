# Generated by Django 5.0.2 on 2024-04-04 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_rename_description_subject_main_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subj_description',
            field=models.CharField(max_length=200),
        ),
    ]