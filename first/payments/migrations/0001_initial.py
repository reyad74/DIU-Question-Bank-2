# Generated by Django 4.2 on 2023-05-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pay_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_id', models.IntegerField()),
                ('pay_option', models.CharField(max_length=25)),
                ('min_pay', models.IntegerField()),
            ],
        ),
    ]
