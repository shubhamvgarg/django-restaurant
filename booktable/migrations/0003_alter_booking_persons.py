# Generated by Django 4.2.14 on 2024-07-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0002_alter_booking_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='persons',
            field=models.IntegerField(),
        ),
    ]
