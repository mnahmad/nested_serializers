# Generated by Django 2.2.16 on 2021-07-02 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210702_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='town',
            old_name='name',
            new_name='town_name',
        ),
    ]
