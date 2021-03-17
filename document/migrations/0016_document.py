# Generated by Django 3.1.7 on 2021-03-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0015_auto_20210222_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('output_format', models.CharField(max_length=6)),
                ('document', models.FileField(upload_to='output')),
            ],
        ),
    ]
