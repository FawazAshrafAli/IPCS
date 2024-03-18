# Generated by Django 5.0 on 2024-01-16 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0007_alter_warranty_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedService',
            fields=[
                ('id', models.CharField(editable=False, max_length=13, primary_key=True, serialize=False)),
                ('service_date', models.DateField()),
                ('starting_time', models.TimeField()),
                ('ending_time', models.TimeField()),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ipcs_admin.servicerequest')),
                ('technician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ipcs_admin.technician')),
            ],
        ),
    ]
