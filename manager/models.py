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


class Course(models.Model):
    name = models.CharField(max_length=127, unique=True)
    start_date = models.DateField()

    def __str__(self):
        return self.name


class DingyInstructorAvailability(models.Model):
    course = models.ForeignKey(Course, on_delete=models.deletion.CASCADE,
                               null=False)
    instructor = models.ForeignKey(DingyInstructor,
                                   on_delete=models.deletion.CASCADE,
                                   null=False)
    assigned = models.BooleanField()

    def __str__(self):
        return self.course.name + " - " + self.instructor.name


class Stage(models.Model):
    name = models.CharField(max_length=127, unique=False)
    no_kids = models.IntegerField()
    DIs = models.ManyToOneRel