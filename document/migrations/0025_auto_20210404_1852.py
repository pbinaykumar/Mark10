# Generated by Django 3.1.7 on 2021-04-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0024_auto_20210318_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='available_format',
            name='name',
        ),
    ]
