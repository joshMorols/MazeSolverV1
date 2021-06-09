from django.db import models

class Maze(models.Model):
    filename = models.TextField(blank=True, null=True)
    user = models.TextField(blank=True, null=True)
    maze = models.TextField()