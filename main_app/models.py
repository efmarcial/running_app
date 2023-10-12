from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Person(models.Model):
    
    user = models.ForeignKey(User, verbose_name=("the related user"), on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=user_directory_path,default="user_icon.png")
    wieght = models.FloatField(max_length=255,null=True)
    height = models.FloatField(max_length=255, null=True)
    
class Activity(models.Model):
    
    user = models.ForeignKey(User, verbose_name="the related user", on_delete=models.CASCADE)
    
    activity_type = models.CharField(max_length=255, default="activity name")
    activity_duration = models.FloatField(max_length=500, default=0)
    
    #Store cordinates as charefield since its going to be a string
    location = models.CharField(max_length=255, null=True)
    
    def __str__(self) -> str:
        return self.user.firstname