from django.db import models


class Lesson(models.Model):
    TYPE = (('A', 'Assesment'), ('L','Lesson'))
    title = models.CharField(max_length=40, verbose_name='Lesson Title')
    intro_text = models.CharField(max_length=100, verbose_name='Short Description')
    study_text = models.CharField(max_length=10000, verbose_name='Lesson Study Material')
    type = models.CharField(max_length=1, choices=TYPE, default='L')
    def __str__(self):
        return self.title
