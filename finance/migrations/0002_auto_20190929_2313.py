# Generated by Django 2.2.5 on 2019-09-30 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='type',
            new_name='expense_type',
        ),
    ]
