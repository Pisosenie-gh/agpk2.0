# Generated by Django 3.2.13 on 2022-05-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agpk', '0002_auto_20220520_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='country',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='state',
        ),
        migrations.AlterField(
            model_name='hotels',
            name='name',
            field=models.CharField(default='AGPK', max_length=30),
        ),
    ]
