# Generated by Django 3.2.9 on 2021-11-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='support_type',
            field=models.CharField(default='Help', max_length=30),
        ),
    ]
