from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from uploader.models import Upload
from .change_name import change_name
from UploaderExamensApunts.constants import *
import os

# Delete the file when it is deleted from the admin panel.
@receiver(pre_delete, sender=Upload)
def uploader_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file_upload.delete(False)

# Move the file to the permanent destination.
@receiver(pre_save, sender=Upload)
def move_file(sender, instance, **kwargs):
    if instance.is_correct:
        pass
    # TODO

@receiver(pre_save, sender=Upload)
def rename(sender, instance, **kwargs):
    # Absolute path to the file.
    old_name = os.path.join(MEDIA_ROOT_SAVED, str(instance.file_upload))
    new_name = os.path.join(MEDIA_ROOT_SAVED, change_name(instance, old_name))

    # Check if the name has changed.
    if old_name != new_name:
        pass
        #os.rename(old_name, new_name)
        # The database should be updated too.
    # TODO