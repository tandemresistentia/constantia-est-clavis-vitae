# Generated by Django 4.1.5 on 2023-03-27 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainlobby', '0012_alter_order_complete_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='license_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
