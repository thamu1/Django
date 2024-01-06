# Generated by Django 4.2.3 on 2024-01-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0013_purchase_details_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase_details',
            old_name='invoice',
            new_name='invoice_id',
        ),
        migrations.AlterField(
            model_name='purchase_details',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='purchase_details',
            table='invoice_purchase_details',
        ),
    ]
