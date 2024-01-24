from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Command(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    code = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.name