from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
    

class Question(models.Model):
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.question


class FeedbackDescription(models.Model):
    description = models.TextField(null=True, blank=True)
    overall_rating = models.PositiveSmallIntegerField()
    instance = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description


class Feedback(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.PositiveSmallIntegerField()
    review = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.ForeignKey(FeedbackDescription, blank=True, null=True, related_name='feedback_description', on_delete=models.CASCADE)

    def __str__(self) -> str:
         return 'test'