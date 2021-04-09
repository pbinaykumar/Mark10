from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User

class Chat(models.Model):
    room=models.CharField(max_length=5)
    chat=JSONField(default=[
        [
            "Welcome To",
            "New Chat"
        ]
    ])

    def __str__(self):
        return self.room

class Connection_Room(models.Model):
    id = models.AutoField(primary_key=True)
    user1=models.ForeignKey(User,on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    connection_id=models.CharField(max_length=15)
    chat = JSONField(default=[
        [
            "Welcome To",
            "New Chat"
        ]
    ])

    def __str__(self):
        return str(self.user1)