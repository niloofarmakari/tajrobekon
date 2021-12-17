from django.contrib import admin
from .models import Experience, ExperienceCategory


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "category")


@admin.register(ExperienceCategory)
class ExperienceCateogryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
