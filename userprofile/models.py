from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import random
from django.utils import timezone
import string
class Certificate(models.Model):
    user = models.ForeignKey(User,related_name='profile', on_delete=models.CASCADE)
    certificate = models.ImageField(_("image"), upload_to='staticfiles/certificates/')
    course_type = models.ForeignKey('bootcamp.Course',related_name='certificates',on_delete=models.CASCADE,default='1')



    def __str__(self):
        return self.user.username