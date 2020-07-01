from django.db import models
from .base import GeneralTest


class AudioDescriptionPair(models.Model):
    audio = models.FileField(upload_to='audio_description_pair')
    description = models.CharField(max_length=100, verbose_name='Audio Description')
    test = models.ForeignKey('Test4', on_delete=models.CASCADE, related_name='audios')
    

class Test4(GeneralTest):
    # This is a Matching Game for audios and Description
    heading = models.CharField(max_length=40, verbose_name='Heading Text(Optional)', null=True, blank=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='test4')
    subject = models.CharField(max_length=20, default="", null=True, blank = True)

    class Meta:
        verbose_name = "Audios & Description Matching Game"

    def __str__(self):
        return str(self.name)
