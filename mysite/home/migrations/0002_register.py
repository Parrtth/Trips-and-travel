# Generated by Django 5.0.2 on 2024-03-04 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('pass1', models.CharField(max_length=20)),
                ('pass2', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
