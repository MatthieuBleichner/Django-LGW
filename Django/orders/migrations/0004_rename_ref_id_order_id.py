# Generated by Django 5.1.6 on 2025-02-28 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ref_id',
            new_name='id',
        ),
    ]
