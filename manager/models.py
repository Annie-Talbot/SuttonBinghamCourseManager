from enum import Enum

from django.db import models


class Experience:
    levels = [
        (0, "No Experience"),
        (1, "Little Experience"),
        (2, "Competent"),
        (3, "Very Competent"),
    ]


class DingyInstructor(models.Model):
    name = models.CharField(max_length=127, unique=True)
    experience = models.IntegerField(choices=Experience.levels, default=0)

    def __str__(self):
        return self.name


class AssistantInstructor(models.Model):
    name = models.CharField(max_length=127, unique=True)
    experience = models.IntegerField(choices=Experience.levels, default=0)

    def __str__(self):
        return self.name


class Helper(models.Model):
    name = models.CharField(max_length=127, unique=True)
    experience = models.IntegerField(choices=Experience.levels, default=0)

    def __str__(self):
        return self.name
