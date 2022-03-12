# Generated by Django 3.1.2 on 2022-03-12 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bootcamp', '0003_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='exams', to=settings.AUTH_USER_MODEL),
        ),
    ]