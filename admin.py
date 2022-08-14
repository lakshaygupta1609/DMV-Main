from django.contrib import admin
from homepage.models import contact_db, view_license_db, apply_licenses_db, branch_db, exam_result_db, exam_db, law_db, vehicle_db, Profile, traffic_offence_db

# Register your models here.
admin.site.register((contact_db, view_license_db, apply_licenses_db, branch_db, exam_result_db, exam_db, law_db, vehicle_db, Profile, traffic_offence_db))
