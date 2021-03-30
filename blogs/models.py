from django.db import models

# Create your models here.
class blogposts(models.Model):
    Title = models.CharField(max_length=200)
    Subtitle = models.CharField(max_length=400)
    Post = models.CharField(max_length=5000)
    Date = models.DateField()
    Author = models.CharField(max_length=100)

    def __str__(self):
        return self.Title


class contacts(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.EmailField()
    Message = models.CharField(max_length=5000)

    def __str__(self):
        return self.Name
