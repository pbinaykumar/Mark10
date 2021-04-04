from django.db import models
from jsonfield import JSONField

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
