from django.contrib import admin
from .models import Song, Difficulty, Record

class DiffcultyInline(admin.TabularInline):
    model = Difficulty
    extra = 1

class SongAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [DiffcultyInline, DiffcultyInline]
class RecordAdmin(admin.ModelAdmin):
    list_display = ('record', )


admin.site.register(Song, SongAdmin)
admin.site.register(Difficulty)
admin.site.register(Record, RecordAdmin)

# Register your models here.
