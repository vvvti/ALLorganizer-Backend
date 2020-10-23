from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Protocol(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    protocol_type = models.CharField("Typ protokołu", max_length=20)
    start_date = models.DateField("Data rozpoczecia")
    end_date = models.DateTimeField("Data zakończenia")
    supp_treatment_start = models.DateTimeField("Data rozpoczęcia podtrzymania")
    is_active = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Protokół"
        verbose_name_plural = "Protokoły"

    def __str__(self):
        return str(self.protocol_type)