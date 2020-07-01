from django.db import models
from .base import GeneralTest


class TextPair(models.Model):
    first = models.CharField(max_length=250)
    second = models.CharField(max_length=250)
    test = models.ForeignKey(
        'Test9', on_delete=models.CASCADE, related_name='questions')


class Test9(GeneralTest):
    # This is a Matching Game for Texts
    heading = models.CharField(
        max_length=200, verbose_name='Heading Text(Optional)', null=True, blank=True)
    lesson = models.ForeignKey(
        'Lesson', on_delete=models.CASCADE, related_name='test9')
    subject = models.CharField(max_length=20, default="", null=True, blank = True)

    class Meta:
        verbose_name = "Text Pair Matching Game"

    def __str__(self):
        return str(self.name)
