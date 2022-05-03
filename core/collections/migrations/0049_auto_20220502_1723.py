# Generated by Django 4.0.3 on 2022-05-02 17:23

from django.db import migrations


def populate_reference_resource_type(apps, schema_editor):
    CollectionReference = apps.get_model('collections', 'CollectionReference')
    CollectionReference.objects.filter(expression__icontains="/mappings/").update(reference_type='mappings')
    CollectionReference.objects.filter(expression__icontains="/concepts/").update(reference_type='concepts')


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0048_collectionreference_cascade_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_reference_resource_type)
    ]