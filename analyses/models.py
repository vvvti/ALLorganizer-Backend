from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CrpAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    crp_date = models.DateField(
        "Data badania")
    crp_time = models.TimeField("Godzina badania", auto_now=False, auto_now_add=False)
    crp_count = models.DecimalField(
        "Wynik CRP", max_digits=4, decimal_places=2)
    is_active = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-crp_date',)
        verbose_name = "Badanie CRP"
        verbose_name_plural = "Badania CRP"

    def __str__(self):
        return str(self.crp_date)


class CompleteBloodCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cbc_date = models.DateField(
        "Data badania")
    cbc_time = models.TimeField("Godzina badania", auto_now=False, auto_now_add=False)
    leucocyte_count = models.DecimalField(
        "Liczba leukocytów", max_digits=8, decimal_places=2)
    erythrocyte_count = models.DecimalField(
        "Erytrocyty", blank=True, null=True, max_digits=4, decimal_places=2)
    hemoglobin = models.DecimalField(
        "Hemoglobina", max_digits=3, decimal_places=1)
    hematocrit = models.DecimalField(
        "Hematokryt", max_digits=3, decimal_places=1)
    mcv = models.DecimalField(
        "MCV", blank=True, null=True, max_digits=4, decimal_places=1)
    mch = models.DecimalField(
        "MCH", blank=True, null=True, max_digits=3, decimal_places=1)
    mchc = models.DecimalField(
        "MCHC", blank=True, null=True, max_digits=3, decimal_places=1)
    thrombocyte_count = models.DecimalField(
        "Płytki krwi", max_digits=3, decimal_places=0)
    rdw_sd = models.DecimalField(
        "RDW-SD", blank=True, null=True, max_digits=3, decimal_places=1)
    rdw_cv = models.DecimalField(
        "RDW-CV", blank=True, null=True, max_digits=3, decimal_places=1)
    pdw = models.DecimalField(
        "PDW", blank=True, null=True, max_digits=3, decimal_places=1)
    mpv = models.DecimalField(
        "MPV", blank=True, null=True, max_digits=3, decimal_places=1)
    p_lcr = models.DecimalField(
        "P-LCR", blank=True, null=True, max_digits=3, decimal_places=1)
    pct = models.DecimalField(
        "PCT", blank=True, null=True, max_digits=3, decimal_places=1)
    neutrophils = models.DecimalField(
        "Neutrofile", max_digits=3, decimal_places=1)
    lymphocytes = models.DecimalField(
        "Limfocyty", blank=True, null=True, max_digits=3, decimal_places=1)
    monocytes = models.DecimalField(
        "Monocyty", blank=True, null=True, max_digits=3, decimal_places=1)
    eosinophils = models.DecimalField(
        "Eozynofile", blank=True, null=True, max_digits=3, decimal_places=1)
    baso = models.DecimalField(
        "Bazofile", blank=True, null=True, max_digits=3, decimal_places=1)
    notes = models.CharField("Uwagi", max_length=200, blank=True)    
    is_active = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-cbc_date',)
        verbose_name = "Morfologia krwi"
        verbose_name_plural = "Morfologie krwi"

    def __str__(self):
        return str(self.cbc_date)

class ALT_AST(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alt_ast_date = models.DateField(
        "Data badania")
    alt_ast_time = models.TimeField("Godzina badania", auto_now=False, auto_now_add=False)
    alt = models.DecimalField("ALT", max_digits=4, decimal_places=0)
    ast = models.DecimalField("AST", max_digits=4, decimal_places=0)    
    is_active = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-alt_ast_date',)
        verbose_name = "Badanie ALT, AST"
        verbose_name_plural = "Badania ALT, AST"

    def __str__(self):
        return str(self.alt_ast_date)


class UrineAnalisis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    urine_date = models.DateField(
        "Data badania")
    urine_time = models.TimeField("Godzina badania", auto_now=False, auto_now_add=False)
    color = models.CharField("Kolor", max_length=45)
    specific_gravity = models.DecimalField(
        "Ciężar właściwy", max_digits=5, decimal_places=4)
    ph = models.DecimalField("PH", max_digits=3, decimal_places=1)
    gluccose = models.CharField(
        "Glukoza", max_length=45, blank=True)
    ketone_bodies = models.CharField(
        "Ketony", max_length=45, blank=True)
    urobilinogen = models.CharField(
        "Urobilinogen", max_length=45, blank=True)
    bilurbin = models.CharField(
        "Bilurbina", max_length=45, blank=True)
    protein = models.CharField("Białko", max_length=45, blank=True)
    erythrocyte = models.CharField(
        "Erytrocyty", max_length=45, blank=True)
    leucocyte = models.CharField(
        "Leukocyty", max_length=45, blank=True)
    bacterial = models.CharField(
        "Bakterie", max_length=45, blank=True)
    notes = models.CharField("Uwagi", max_length=200, blank=True)    
    is_active = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-urine_date',)
        verbose_name = "Badanie Moczu"
        verbose_name_plural = "Badania Moczu"

    def __str__(self):
        return str(self.urine_date)
