# Generated by Django 3.1.7 on 2021-03-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0018_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='output_format',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
