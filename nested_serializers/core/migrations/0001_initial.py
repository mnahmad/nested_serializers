# Generated by Django 2.2.16 on 2021-06-30 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
                ('bok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rbook', to='core.Book')),
            ],
        ),
    ]
