# Generated by Django 4.2.1 on 2023-06-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autodrawing_app', '0003_comic_comment_page_comic_content_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateselect',
            name='numpage',
            field=models.IntegerField(default=1),
        ),
    ]
