# Generated by Django 3.1.2 on 2022-03-12 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20220312_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='chat_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='final_score',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]