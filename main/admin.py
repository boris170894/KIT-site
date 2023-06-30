from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import CollegeContactModel, CollegeHistoryModel, CollegePartnersModel

@admin.register(CollegeHistoryModel)
class CollegeHistoryAdmin(TranslationAdmin):
    list_display = ('year',)

@admin.register(CollegeContactModel)
class CollegeContactAdmin(TranslationAdmin):
    list_display = ('addr',)

@admin.register(CollegePartnersModel)
class CollegePartnersAdmin(TranslationAdmin):
    list_display = ('partner_name',)