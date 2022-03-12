from django.contrib import admin
from .models import Course,UserCourse,Exam
from import_export.admin import ExportActionMixin
from django.contrib.auth.models import User
from import_export import resources
# Register your models here.
admin.site.register(Course)
admin.site.register(UserCourse)


class BookResource(resources.ModelResource):

    class Meta:
        model = Exam
        widgets = {
                'user': {'format': 'user__username'},
                }
class ExamAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('exam_user','question_1','question_2','question_3', 'question_4', 'question_5', 'question_6' ,'question_7' ,'question_8' ,'question_9')
    # ,'question_2' 'question_3' 'question_4' 'question_5' 'question_6' 'question_7' 'question_8' 'question_9'

admin.site.register(Exam, ExamAdmin)

