# Generated by Django 2.2.5 on 2019-09-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_remove_expense_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
