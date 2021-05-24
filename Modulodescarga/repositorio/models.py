from django.db import models

# Create your models here.
class Files(models.Model):
    id_file = models.IntegerField
    name = models.CharField(max_length=1000)
    date = models.DateField()
    state =  models.CharField(max_length=300)
    def __str__(self):
        return self.name

class State_dictionary(models.Model):
    id_state = models.IntegerField()
    state_name = models.CharField(max_length=500)

class User(models.Model):
    id_user = models.IntegerField()
    user_name = models.CharField(max_length=500)
    state = models.CharField(max_length=400)