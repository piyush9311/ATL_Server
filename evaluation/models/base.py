from django.db import models


class GeneralTest(models.Model):
    name = models.CharField(max_length=20)
