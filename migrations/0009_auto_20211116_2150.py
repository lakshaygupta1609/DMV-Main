# Generated by Django 3.2.9 on 2021-11-16 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20211116_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view_license',
            name='name',
        ),
        migrations.RemoveField(
            model_name='view_license',
            name='username',
        ),
    ]
