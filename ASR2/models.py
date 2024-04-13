from django.db import models

class Instance(models.Model):
    ip = models.CharField()