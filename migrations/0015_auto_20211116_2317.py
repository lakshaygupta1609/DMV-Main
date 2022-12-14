# Generated by Django 3.2.9 on 2021-11-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_remove_exam_exam_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply_license_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('citizenship', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('vehicle_type', models.CharField(choices=[('Learner', 'Learner'), ('Two-Wheeler', 'Two-Wheeler'), ('Four-Wheeler', 'Four-Wheeler')], max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('application_date', models.DateTimeField()),
                ('applicant_email', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='branch',
            new_name='branch_db',
        ),
        migrations.RenameModel(
            old_name='exam',
            new_name='exam_db',
        ),
        migrations.RenameModel(
            old_name='exam_result',
            new_name='exam_result_db',
        ),
        migrations.RenameModel(
            old_name='law',
            new_name='law_db',
        ),
        migrations.RenameModel(
            old_name='traffic_offence',
            new_name='traffic_offence_db',
        ),
        migrations.RenameModel(
            old_name='vehicle',
            new_name='vehicle_db',
        ),
        migrations.RenameModel(
            old_name='view_license',
            new_name='view_license_db',
        ),
        migrations.DeleteModel(
            name='apply_license',
        ),
    ]
