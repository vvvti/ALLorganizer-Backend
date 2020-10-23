from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class MedicineDose(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Nazwa lekarstwa", max_length=80)
    dose = models.DecimalField("Dawka", max_digits=6, decimal_places=2)
    start_date = models.DateTimeField("Rozpoczecie zażywania")
    end_date = models.DateTimeField("Zakończenie zażywania")
    notes = models.CharField("Uwagi", max_length=200, blank=True)
    is_active = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ('start_date',)
        verbose_name = "Dawka lekarstwa"
        verbose_name_plural = "Dawki lekarstw"

    def __str__(self):
        return str(self.start_date)