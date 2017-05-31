
from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 50)

    def __str__(self):
        return "{name} {last_name}".format(name=self.name,last_name=self.last_name)

class Type(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length = 50)
    director = models.ForeignKey(Director)
    type = models.ForeignKey(Type)
    production_date = models.DateField(null=True)

    def __str__(self):
        return "{title} {director} {type} {production_date}".format(title=self.title, director=self.director, type=self.type,production_date=self.production_date)