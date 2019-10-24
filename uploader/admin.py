from django.contrib import admin
from uploader.models import Upload, Person

class UploadAdmin(admin.ModelAdmin):
    list_display = ('upload_date', 'grau', 'file_upload', 'is_correct')
    exclude = ()

class PersonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'dni', 'email')
    exclude = ()

admin.site.register(Upload, UploadAdmin)
admin.site.register(Person, PersonAdmin)
