from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_review = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)