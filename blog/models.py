from django.db import models


# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(TimeStamp):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Author(TimeStamp):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
