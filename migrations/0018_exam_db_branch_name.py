# Generated by Django 3.2.9 on 2021-11-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_auto_20211117_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_db',
            name='branch_name',
            field=models.CharField(default='-', max_length=30),
        ),
    ]