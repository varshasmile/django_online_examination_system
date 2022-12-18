# Model for Questions and Answers

from django.db import models
from django.conf import settings

class Course(models.Model):
    course = models.CharField(max_length=150, unique=True, null=True)

    def __str__(self):
        return self.course

class Paper(models.Model):
    paper = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.paper
    
class Questions(models.Model):
    qs_no=models.IntegerField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True, blank=True)
    questions = models.TextField(null=True)
    answers = models.CharField(max_length=20, null=True)
    option_a = models.TextField(null=True)
    option_b = models.TextField(null=True)
    option_c = models.TextField(null=True)
    option_d = models.TextField(null=True)

    def __str__(self):
        return (str(self.course) + ' ' + str(self.paper) + ' Q.No. ' + str(self.qs_no) + '-' + str(self.questions))
    
class Answer(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.answer

