from django.contrib import admin

from .models import Olympics, OlympicsCategory, Mentor

@admin.register(OlympicsCategory)
class OlympicsCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    pass

@admin.register(Olympics)
class OlympicsAdmin(admin.ModelAdmin):
    pass
