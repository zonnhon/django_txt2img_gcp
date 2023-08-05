from django.db import models

# Create your models here.

class DateSelect(models.Model):
    datestr = models.CharField(max_length=255)
    newspage = models.IntegerField(default=1)
    gamepage = models.IntegerField(default=1)
    comicpage = models.IntegerField(default=1)
    class Meta:
        db_table = 'dateselect'

class News_content(models.Model):
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()
    page = models.IntegerField(default=0)
    class Meta:
        db_table = 'news_content'

class News_comment(models.Model):
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()
    page = models.IntegerField(default=0)
    class Meta:
        db_table = 'news_comment'


class Game_content(models.Model):
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()
    page = models.IntegerField(default=0)

    class Meta:
        db_table = 'game_content'


class Game_comment(models.Model):
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()
    page = models.IntegerField(default=0)

    class Meta:
        db_table = 'game_comment'

class Comic_content(models.Model):
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()
    page = models.IntegerField(default=0)

    class Meta:
        db_table = 'comic_content'


class Comic_comment(models.Model):
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()
    page = models.IntegerField(default=0)

    class Meta:
        db_table = 'comic_comment'