from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-id']