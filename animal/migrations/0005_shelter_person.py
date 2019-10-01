# Generated by Django 2.2.5 on 2019-10-01 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
        ('animal', '0004_auto_20190928_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='person',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='contacts.Contact', verbose_name='Pessoa'),
            preserve_default=False,
        ),
    ]
