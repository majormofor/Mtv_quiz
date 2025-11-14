from django.db import models
from django.utils import timezone
# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=15, unique=True)
    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)  # new field

    class Meta:
        ordering = ['-score', 'submitted_at']  # high scores first, then earliest submission

    def __str__(self):
        return f"{self.name} - {self.phone_number} ({self.score})"


    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.score}"
    
class Question(models.Model):
    question_text = models.TextField()
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1)  # A, B, C, or D

    def __str__(self):
        return self.question_text