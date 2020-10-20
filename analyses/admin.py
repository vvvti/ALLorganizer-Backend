from django.contrib import admin
from .models import CompleteBloodCount, CrpAnalysis, UrineAnalisis, ALT_AST

admin.site.register(CompleteBloodCount)
admin.site.register(CrpAnalysis)
admin.site.register(UrineAnalisis)
admin.site.register(ALT_AST)