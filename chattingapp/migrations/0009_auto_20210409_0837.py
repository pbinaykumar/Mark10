# Generated by Django 3.1.7 on 2021-04-09 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chattingapp', '0008_auto_20210409_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection_room',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='connection_room',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='auth.user'),
        ),
    ]