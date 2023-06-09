# Generated by Django 4.1.5 on 2023-04-01 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainlobby', '0019_order_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Delivered', 'Delivered'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='license_file',
            field=models.FileField(blank=True, null=True, upload_to='myfiles/'),
        ),
    ]
