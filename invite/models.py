from django.db import models

class SentToken(models.Model):
    token = models.CharField(max_length=384)
    user_id = models.CharField(max_length=20)
