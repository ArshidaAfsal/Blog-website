# Generated by Django 5.1.4 on 2025-01-03 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_comment_profile_pic_post_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='profile_picture',
            new_name='profile_pic',
        ),
    ]
