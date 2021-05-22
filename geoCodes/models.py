from django.db import models

# Create your models here.
class GeogInfo(models.Model):
    GeogCode_id = models.BigAutoField(primary_key = True)
    longitude = models.DecimalField( max_digits=22, decimal_places=16)
    latitude = models.DecimalField( max_digits=22, decimal_places=16)
    timezone = models.CharField(max_length=150,blank=True, null=True)
    current_date = models.DateField()
    current_sunrise = models.DateField()
    current_sunset = models.DateField()
    current_temp = models.DecimalField(max_digits=5,decimal_places=3)

    class Meta:
        ordering = ['GeogCode_id']