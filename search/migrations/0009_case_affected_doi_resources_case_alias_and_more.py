# Generated by Django 5.1 on 2025-01-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_document_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='affected_doi_resources',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='alias',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='authority',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='contaminants_of_concern',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='incident_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
