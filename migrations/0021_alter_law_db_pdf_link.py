# Generated by Django 3.2.9 on 2021-11-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0020_traffic_offence_db_fee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='law_db',
            name='pdf_link',
            field=models.CharField(max_length=256),
        ),
    ]
