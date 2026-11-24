from django.db import models

# Create your models here.
class Scenario(models.Model):
    description = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)

    def __str__(self):
        return self.description