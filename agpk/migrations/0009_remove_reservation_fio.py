# Generated by Django 3.2.13 on 2022-06-14 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agpk', '0008_reservation_fio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='FIO',
        ),
    ]
