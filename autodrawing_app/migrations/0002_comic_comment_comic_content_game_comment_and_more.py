# Generated by Django 4.2.1 on 2023-05-31 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autodrawing_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comic_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=8291)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'comic_comment',
            },
        ),
        migrations.CreateModel(
            name='Comic_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=8291)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'comic_content',
            },
        ),
        migrations.CreateModel(
            name='Game_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=8291)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'game_comment',
            },
        ),
        migrations.CreateModel(
            name='Game_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=8291)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'game_content',
            },
        ),
        migrations.CreateModel(
            name='News_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=8291)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'news_comment',
            },
        ),
        migrations.CreateModel(
            name='News_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=8291)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'news_content',
            },
        ),
    ]
