from django.db import models

# Create your models here.
# class Movies(models.Model):
#     tittle = models.CharField(max_length = 100)
#     year = models.IntegerField()
#     def __str__(self):
#         return f'{self.tittle }from {self.year} '
class Movie(models.Model):
    tittle = models.CharField(max_length = 100)
    year = models.IntegerField()
    description = models.TextField(max_length = 100)


    def __str__(self):
        return self.tittle
