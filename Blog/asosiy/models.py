from django.db import models

# Create your models here.
class Maqola(models.Model):
    sana = models.DateField()
    sarlavha = models.CharField(max_length=150)
    matn = models.TextField()
    rasm = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.sarlavha

class Talk(models.Model):
    sana = models.DateField()
    sarlavha = models.CharField(max_length=200)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.sarlavha