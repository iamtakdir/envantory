# Generated by Django 3.1.7 on 2021-03-05 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20210306_0137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='ammount',
            new_name='amount',
        ),
    ]