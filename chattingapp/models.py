from django.db import models
from jsonfield import JSONField

class Chat(models.Model):
    path=models.CharField(max_length=5)
    chat=models.JSONField()

    def __str__(self):
        return self.path
