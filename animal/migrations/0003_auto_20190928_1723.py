# Generated by Django 2.2.5 on 2019-09-28 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_auto_20190928_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinical_condition', models.CharField(max_length=55, verbose_name='Estado Clínico')),
                ('date', models.DateField(verbose_name='Data')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal', verbose_name='Animal')),
            ],
        ),
        migrations.DeleteModel(
            name='HealthLog',
        ),
    ]
