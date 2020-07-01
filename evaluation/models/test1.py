from django.db import models
from .base import GeneralTest


class Option(models.Model):
    # This model Defines a Multiple Correct Options Question Choices
    text = models.CharField(max_length=100, verbose_name='Option')
    correct = models.BooleanField()
    question = models.ForeignKey(
        'Question', on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return 'Option Text: ' + str(self.text)


class Question(models.Model):
    # This model Defines a Multiple Correct Options Question
    image = models.ImageField(
        upload_to="multiple_choice_question_image", null=True, blank=True)
    youtube_video = models.CharField(max_length=200, default='', null=True, blank=True, verbose_name="Youtube Video (Will Replace Image)")
    test = models.ForeignKey(
        'Test1', on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=200, verbose_name='Question')

    class Meta:
        verbose_name = "Multiple Choice Question"

    def __str__(self):
        return str(self.test.name + ' | ' + self.text)


class Test1(GeneralTest):
    # This model Defines a Multiple Correct Options Test
    heading = models.CharField(
        max_length=200, verbose_name='Heading Text(Optional)', null=True, blank=True)
    lesson = models.ForeignKey(
        'Lesson', on_delete=models.CASCADE, related_name='test1')
    subject = models.CharField(max_length=20, default="", null=True, blank = True)
    class Meta:
        verbose_name = "Multiple Choice Test"

    def __str__(self):
        return str(self.name)
