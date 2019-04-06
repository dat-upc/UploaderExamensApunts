from django.db.models.signals import pre_delete, post_save
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

# Change the file name if an admin makes some changes.
@receiver(post_save, sender=Upload)
def move_file(sender, instance, **kwargs):
    # Absolute path to the file.
    old_name = os.path.join(MEDIA_ROOT_SAVED, instance.file_upload.name)
    if instance.is_correct:
        new_name = os.path.join(ABS_FINAL_DIR, os.path.basename(change_name(instance, os.path.basename(old_name))))
        created = False
        dest_dir = REL_FINAL_DIR
    else:
        new_name = os.path.join(MEDIA_ROOT_SAVED, change_name(instance, os.path.basename(old_name)))
        created = kwargs.get('created')
        dest_dir = REL_TMP_DIR

    # Check if the name has changed.
    if old_name != new_name and not created and not hasattr(instance, '_dirty'):
        instance.file_upload.name = os.path.join(dest_dir, os.path.basename(new_name))
        try:
            instance._dirty = True
            instance.save()
            # Check if the destination directory exists.
            if not os.path.exists(os.path.dirname(new_name)):
                os.makedirs(os.path.dirname(new_name))
            os.rename(old_name, new_name)
        finally:
            del instance._dirty
