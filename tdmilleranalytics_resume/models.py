from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class ResumeHeader(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = RichTextField()
    def __str__(self):
        return self.title

class ResumeCategory(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class ResumeItemLong(models.Model):
    resume_category = models.ForeignKey(ResumeCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30)
    organization = models.CharField(max_length=30, null=True, blank=True)
    start = models.CharField(max_length=20, null=True, blank=True)
    end = models.CharField(max_length=20, null=True, blank=True)
    description = RichTextField()
    def __str__(self):
        return self.title

class ResumeItemShort(models.Model):
    resume_category = models.ForeignKey(ResumeCategory, on_delete=models.SET_NULL, null=True)
    item_text = models.CharField(max_length=45)
    rating_percent = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.item_text
