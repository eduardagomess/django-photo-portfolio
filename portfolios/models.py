from django.db import models


class Portfolio(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  date = models.CharField(max_length=20)
  camera = models.CharField(max_length=20)
  photo_editor = models.TextField()
  photographer = models.CharField(max_length=20)
  contact = models.TextField()
  image = models.FilePathField(path="static/img")
