# Generated by Django 3.1.7 on 2021-03-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0020_auto_20210313_0553'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Input_File',
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='media/output'),
        ),
    ]
