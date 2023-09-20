from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
                        CollegeContactModel, 
                        CollegeHistoryModel, 
                        CollegePartnersModel,
                        CollegeDocsModel,
                        StateSymbolsModel
                     )

@admin.register(CollegeHistoryModel)
class CollegeHistoryAdmin(TranslationAdmin):
    list_display = ('year',)

@admin.register(CollegeContactModel)
class CollegeContactAdmin(TranslationAdmin):
    list_display = ('addr',)

@admin.register(CollegePartnersModel)
class CollegePartnersAdmin(TranslationAdmin):
    list_display = ('partner_name',)
    
admin.site.register(CollegeDocsModel)

@admin.register(StateSymbolsModel)
class StateSymbolsAdmin(TranslationAdmin):
    list_display = ('name', 'image',)