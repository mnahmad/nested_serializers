# Generated by Django 2.2.16 on 2021-07-02 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_country_state_town'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='name',
            new_name='cntry_name',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='name',
            new_name='state_name',
        ),
    ]
