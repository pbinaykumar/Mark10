# Generated by Django 3.1.7 on 2021-04-04 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0025_auto_20210404_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='available_format',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.file_type'),
        ),
    ]