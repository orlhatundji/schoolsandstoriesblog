# Generated by Django 2.2.8 on 2019-12-21 23:48

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191221_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='Content'),
            preserve_default=False,
        ),
    ]
