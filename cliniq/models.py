
from django.db import models


class Spécialité (models.Model):
    nom = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom

class Spécialiste (models.Model):
    nom = models.CharField(max_length=200)
    prénom = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=100)
    spécialité = models.ForeignKey(Spécialité, on_delete=models.CASCADE)
    nbr_max_rdv = models.IntegerField()

    def __str__(self):
        return self.nom



class Gérent(models.Model):
    nom = models.CharField(max_length=200)
    prénom = models.CharField(max_length=200)
    email =models.EmailField(max_length=40)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Patient(models.Model):
    nom = models.CharField(max_length=200)
    prénom = models.CharField(max_length=200)
    age = models.IntegerField(null = True )
    Tél = models.CharField(max_length=8)
    

    def __str__(self):
        return self.nom


class RDV (models.Model):
    spécialiste =models.ForeignKey(Spécialiste, on_delete=models.CASCADE) 
    date = models.DateField()
    temp = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
     


