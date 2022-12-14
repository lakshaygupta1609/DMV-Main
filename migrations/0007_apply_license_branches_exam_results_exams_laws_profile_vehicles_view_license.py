# Generated by Django 3.2.9 on 2021-11-15 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0006_contact_db_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply_license',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('citizenship', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('vehicle_type', models.CharField(choices=[('L', 'Learner'), ('Two', '2-Wheeler'), ('Four', '4-Wheeler')], max_length=4)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('branch_name', models.CharField(max_length=30)),
                ('hours', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='exam_results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('exam_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('exam_time', models.DateTimeField()),
                ('exam_type', models.CharField(choices=[('W', 'Written'), ('P', 'Practical')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='laws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_link', models.CharField(max_length=30)),
                ('law_name', models.CharField(max_length=30)),
                ('law_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_model', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('vehicle_type', models.CharField(choices=[('Two', '2-Wheeler'), ('Four', '4-Wheeler'), ('Many', 'Many-Wheeler')], max_length=5)),
                ('license_plate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='view_license',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('citizenship', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('vehicle_type', models.CharField(choices=[('L', 'Learner'), ('Two', '2-Wheeler'), ('Four', '4-Wheeler')], max_length=4)),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizenship', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
