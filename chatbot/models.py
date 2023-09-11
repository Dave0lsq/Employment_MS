from django.db import models


# Create your models here.
class EssayQuestion(models.Model):
    question_text = models.TextField()

    year_choices = [
        (1, '2012'),
        (2, '2013'),
        (3, '2014'),
        (4, '2015'),
        (5, '2016'),
        (6, '2017'),
        (7, '2018'),
        (8, '2019'),
        (9, '2020'),
        (10, '2021'),
        (11, '2022'),
        (12, '2023'),
    ]

    year = models.SmallIntegerField(choices=year_choices)

    def __str__(self):
        return f"{self.question_text[:100]} - {self.year}"
