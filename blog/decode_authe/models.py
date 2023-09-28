from django.db import models
from django.contrib.auth.models import User
import uuid

def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'avatars/{new_file_name}'

