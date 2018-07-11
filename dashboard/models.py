from django.db import models

# Create your models here.


class Place(models.Model):
    name_place = models.CharField(max_length = 100)
    def __str__(self):
        return self.name_place

class Time(models.Model):
    name_time = models.CharField(max_length = 50)
    place = models.ForeignKey(Place, default = None,on_delete = models.CASCADE)
    def __str__(self):
        return self.name_time
    
class Meal(models.Model):
    name_meal = models.CharField(max_length = 200)
    price_meal = models.FloatField()
    availability_meal = models.IntegerField()
    time = models.ForeignKey(Time, on_delete = models.CASCADE) #relacion entre los modelos Meal y Time, cada turno tiene diferentes comidas
    #tipo_meal = models.IntegerField(default=0)
    #1=>Almidon u harinas 2=>Ensalada 3=>Menestra 4=>Carnes
    #quantity_meal = models.IntegerField(default = 0)
    def __str__(self):
        return self.name_meal

class Suggestion(models.Model):
    text_suggestion = models.CharField(max_length = 500)
    place = models.ForeignKey(Place, on_delete = models.CASCADE)