from django.db import models

# Create your models here.
class Questions1(models.Model):
    nbr = models.IntegerField(unique=True, blank=True, null=True)
    question = models.CharField(max_length=250)

    option1 = models.CharField(max_length=100, blank=True, null=True)
    option2 = models.CharField(max_length=100, blank=True, null=True)
    option3 = models.CharField(max_length=100, blank=True, null=True)
    option4 = models.CharField(max_length=100, blank=True, null=True)

    answer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.question

class Questions2(models.Model):
    nbr = models.IntegerField(unique=True, blank=True, null=True)
    question = models.CharField(max_length=250)

    option1 = models.CharField(max_length=100, blank=True, null=True)
    option2 = models.CharField(max_length=100, blank=True, null=True)
    option3 = models.CharField(max_length=100, blank=True, null=True)
    option4 = models.CharField(max_length=100, blank=True, null=True)

    answer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.question
