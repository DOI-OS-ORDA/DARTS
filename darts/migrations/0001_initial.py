# Generated by Django 5.1 on 2024-12-18 02:54

import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('file', models.BinaryField()),
                ('body', models.TextField()),
                ('search_text', django.contrib.postgres.search.SearchVectorField()),
            ],
        ),
    ]