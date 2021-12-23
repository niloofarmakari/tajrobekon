from django.contrib import admin
from .models import Experience, ExperienceCategory, ExperienceComment


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(ExperienceCategory)
class ExperienceCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ExperienceComment)
class ExperienceCommentAdmin(admin.ModelAdmin):
    pass
