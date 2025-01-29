# Generated by Django 4.2 on 2025-01-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_location_address_alter_location_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Organizer',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='Domyślny opis'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
