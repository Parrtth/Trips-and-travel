# Generated by Django 5.0.2 on 2024-03-31 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='tour-images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
