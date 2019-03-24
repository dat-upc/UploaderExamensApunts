from django.contrib import admin
from uploader.models import Upload

class UploadAdmin(admin.ModelAdmin):
    list_display = ('upload_date', 'file_upload', 'is_correct')
    exclude = ()

admin.site.register(Upload, UploadAdmin)
