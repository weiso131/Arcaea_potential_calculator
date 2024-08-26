from django.contrib import admin
from .models import Song, Difficulty

class DiffcultyInline(admin.TabularInline):
    model = Difficulty
    extra = 1

class SongAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [DiffcultyInline, DiffcultyInline]



admin.site.register(Song, SongAdmin)
admin.site.register(Difficulty)

# Register your models here.
