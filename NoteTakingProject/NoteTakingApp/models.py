from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
