# Generated by Django 4.2.14 on 2024-07-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
