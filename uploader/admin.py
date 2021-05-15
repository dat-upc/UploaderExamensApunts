# Copyright (C) 2019 Aniol Marti
# This file is part of DAT - UploaderExamensApunts.
#
# DAT - UploaderExamensApunts is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DAT - UploaderExamensApunts is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with DAT - UploaderExamensApunts. If not, see <https://www.gnu.org/licenses/>.
#
from django.contrib import admin
from uploader.models import Upload, Person, Degree, Subject, ExamType, DocumentType, ExamWeight

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('nom_curt', 'nom')
    exclude = ()

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('nom', 'grau')
    exclude = ()

class ExamTypeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    exclude = ()

class ExamWeightAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    exclude = ()

class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    exclude = ()

class UploadAdmin(admin.ModelAdmin):
    list_display = ('upload_date', 'grau', 'assignatura', 'file_upload', 'is_correct')
    exclude = ()

class PersonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'dni', 'email')
    exclude = ()

admin.site.register(Degree, DegreeAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(ExamType, ExamTypeAdmin)
admin.site.register(ExamWeight, ExamWeightAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Upload, UploadAdmin)
admin.site.register(Person, PersonAdmin)
