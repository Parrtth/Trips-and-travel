# Generated by Django 5.0.2 on 2024-05-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname_booking', models.CharField(max_length=20)),
                ('lastname_booking', models.CharField(max_length=20)),
                ('email_booking', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=10)),
                ('firstname_card', models.CharField(max_length=20)),
                ('card_number', models.CharField(max_length=12)),
                ('expire_month', models.DateField()),
                ('expire_year', models.DateField()),
                ('ccv', models.DateField(max_length=12)),
                ('country', models.CharField(max_length=20)),
                ('street_1', models.CharField(max_length=50)),
                ('street_2', models.CharField(max_length=50)),
                ('city_booking', models.CharField(max_length=15)),
                ('state_booking', models.CharField(max_length=20)),
                ('postal_code', models.CharField(max_length=6)),
                ('message', models.TextField()),
            ],
        ),
    ]
