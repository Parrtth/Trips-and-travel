# Generated by Django 5.0.2 on 2024-04-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='profile-images/'),
        ),
    ]
