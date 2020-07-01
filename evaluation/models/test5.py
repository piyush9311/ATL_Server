from django.db import models
from .base import GeneralTest


class ImageOption(models.Model):
    # This model Defines a Multiple Correct Options Question Choices
    image = models.ImageField(upload_to="muliple_choice_images")
    text = models.CharField(max_length=50, verbose_name='Option')
    correct = models.BooleanField()
    question = models.ForeignKey('ImageQuestion', on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return 'Option Text: ' + str(self.text)


class ImageQuestion(models.Model):
    # This model Defines a Multiple Correct Options Question
    test = models.ForeignKey('Test5', on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=200, verbose_name='Question')

    class Meta:
        verbose_name = "Multiple Choice Question with Image"

    def __str__(self):
        return str(self.text)


class Test5(GeneralTest):
    # This model Defines a Multiple Correct Options Test
    heading = models.CharField(max_length=40, verbose_name='Heading Text(Optional)', null=True, blank=True)
    subject = models.CharField(max_length=20, default="", null=True, blank = True)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='test5')

    class Meta:
        verbose_name = "Multiple Choice Test with Image"

    def __str__(self):
        return str(self.name)
