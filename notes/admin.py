from django.contrib import admin

from . import models


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', )


# Register that that model is attached to this admin model
admin.site.register(models.Notes, NotesAdmin)
