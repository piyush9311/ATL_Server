from django.db import models
from .base import GeneralTest


class PictureTextInput(models.Model):
    picture = models.ImageField(upload_to='picture_text_input')
    correct_text = models.CharField(
        max_length=100, verbose_name='Correct Input for Image')
    test = models.ForeignKey(
        'Test6', on_delete=models.CASCADE, related_name='pictures')


class Test6(GeneralTest):
    # This is a Matching Game for pictures and Description
    heading = models.CharField(
        max_length=100, verbose_name='Heading Text(Optional)', null=True, blank=True)
    lesson = models.ForeignKey(
        'Lesson', on_delete=models.CASCADE, related_name='test6')
    subject = models.CharField(max_length=20, default="", null=True, blank = True)

    class Meta:
        verbose_name = "Picture Text Input Puzzle"

    def __str__(self):
        return str(self.name)
