# Generated by Django 2.2.5 on 2019-10-02 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_merge_20191001_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_type',
            field=models.CharField(choices=[('CT', 'Conta de Telefone'), ('CL', 'Conta de Luz'), ('CA', 'Conta de Água'), ('TX', 'Taxi'), ('VT', 'Veterinário'), ('RM', 'Remédios'), ('OT', 'Outros')], max_length=30),
        ),
    ]
