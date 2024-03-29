# Generated by Django 5.0 on 2024-01-17 03:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0015_alter_repairrequest_contact_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairService',
            fields=[
                ('id', models.CharField(editable=False, max_length=13, primary_key=True, serialize=False)),
                ('repair_date', models.DateField()),
                ('starting_time', models.TimeField()),
                ('ending_time', models.TimeField()),
                ('repair_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ipcs_admin.repairrequest')),
                ('technician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ipcs_admin.technician')),
            ],
        ),
    ]
