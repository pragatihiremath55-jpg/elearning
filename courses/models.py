from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    enrolled_courses = models.ManyToManyField('Course', blank=True)

    def __str__(self):
        return self.name