# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Todo'
    verbose_name_plural = 'Todos'
