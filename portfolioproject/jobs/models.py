from django.db import models

class Job(models.Model):
    #images showing what it looks like
    #anztime we work with image we have to install Pillow
    image = models.ImageField(upload_to='images/')
    #text summary with explanation
    summary = models.CharField(max_length=200)

