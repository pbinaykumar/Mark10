# Generated by Django 3.1.7 on 2021-04-03 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chattingapp', '0004_auto_20210404_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='path',
            new_name='room',
        ),
    ]