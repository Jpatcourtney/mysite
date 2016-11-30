from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Activity(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    location = models.CharField(max_length=250)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    orig_url = models.TextField()
    notes = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
        )


    def __str__(self):
        return self.title