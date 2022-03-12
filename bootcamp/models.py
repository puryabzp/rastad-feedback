from distutils.command.build_scripts import first_line_re
from pyexpat import model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from userprofile.models import Certificate
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(_('course name'),max_length=100)
    course_link = models.URLField(_('course link'),unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'),auto_now=True)

    def __str__(self):
        return self.name

class UserCourse(models.Model):
    # courses = [
    #     ('Fund', _('Fundamental')),
    #     ('tech', _('technical')),
    #     ('investmgmt', _('Investment Management')),
    #     ('full',_('full course'))
    # ]
    course = models.ManyToManyField(Course,related_name='users')
    user = models.OneToOneField(User,related_name='courses',on_delete=models.CASCADE,default=0)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'),auto_now=True)
    def __str__(self):
        courses = ''
        for i in self.course.all():
            courses+=f'/{i}'
        return self.user.first_name + " "+ self.user.last_name + ":"+ courses
class Exam(models.Model):
    exam_user = models.ForeignKey(User,related_name='exams',on_delete=models.CASCADE,default=0)
    question_1= models.IntegerField(_('question_1'),blank=True,null=True)  
    question_2=models.IntegerField(_('question_2'),blank=True,null=True) 
    question_3=models.IntegerField(_('question_3'),blank=True,null=True) 
    question_4=models.IntegerField(_('question_4'),blank=True,null=True) 
    question_5=models.IntegerField(_('question_5'),blank=True,null=True) 
    question_6=models.IntegerField(_('question_6'),blank=True,null=True) 
    question_7 =models.IntegerField(_('question_7'),blank=True,null=True) 
    question_8=models.IntegerField(_('question_8'),blank=True,null=True) 
    question_9=models.TextField(_('question_9'),blank=True,null=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'),auto_now=True)    