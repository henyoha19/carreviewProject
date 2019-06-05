from django.db import models


# Create your models here.
class CarMake (models.Model):
    carmakename=models.CharField(max_length=255, null=True, blank=True)
    cardescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.carmakename


class CarModel (models.Model):
    carmodelname=models.CharField(max_length=255)
    Carmake=models.ForeignKey(CarMake, on_delete=models.DO_NOTHING)
    carprice=models.DecimalField(max_digits=10, decimal_places=2)
    manifacturingdate=models.DateField()
    carmillage=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cardescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.carmodelname


class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    CarModel=models.ForeignKey(CarModel, on_delete=models.DO_NOTHING)
    rating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle


