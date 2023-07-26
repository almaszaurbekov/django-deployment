import uuid
from django.db import models
from core.models import User

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.CharField(max_length=200)
    text = models.TextField(null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.topic