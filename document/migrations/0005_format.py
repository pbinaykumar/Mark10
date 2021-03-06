# Generated by Django 3.1.7 on 2021-02-20 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_author_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='photos')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.available_format')),
            ],
        ),
    ]
