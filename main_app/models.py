from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Person(models.Model):
    
    user = models.ForeignKey(User, verbose_name=("the related user"), on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=user_directory_path )