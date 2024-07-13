from django.db import models

class Dictionary(models.Model):

    word = models.CharField(max_length=1000)
    part_of_speech = models.CharField(max_length=1000)
    description = models.TextField()

    def __str__(self):
        return f"{self.word} ({self.part_of_speech})"