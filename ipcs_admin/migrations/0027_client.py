# Generated by Django 5.0.1 on 2024-01-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0026_alter_claimedwarranty_serial_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(default='/static/images/default_images/no_image.jpeg', upload_to='client_images/')),
            ],
        ),
    ]