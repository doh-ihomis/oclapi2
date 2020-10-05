# Generated by Django 3.0.9 on 2020-10-05 06:53

from django.db import migrations
from django.db.models import F


def update_mappings_mnemonic(apps, schema_editor):
    Mapping = apps.get_model('mappings', 'Mapping')
    Mapping.objects.update(mnemonic=F('versioned_object_id'))


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0006_auto_20201005_0649'),
    ]

    operations = [
        migrations.RunPython(update_mappings_mnemonic)
    ]
