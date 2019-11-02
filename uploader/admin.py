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
from uploader.models import Upload, Person

class UploadAdmin(admin.ModelAdmin):
    list_display = ('upload_date', 'grau', 'file_upload', 'is_correct')
    exclude = ()

class PersonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'dni', 'email')
    exclude = ()

admin.site.register(Upload, UploadAdmin)
admin.site.register(Person, PersonAdmin)
