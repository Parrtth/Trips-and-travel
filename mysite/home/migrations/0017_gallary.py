# Generated by Django 5.0.2 on 2024-04-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_program_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img', models.ImageField(upload_to='gallary/')),
            ],
        ),
    ]
