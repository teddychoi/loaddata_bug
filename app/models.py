from django.db import models

class TestClass(models.Model):
    name = models.CharField(max_length=10)
