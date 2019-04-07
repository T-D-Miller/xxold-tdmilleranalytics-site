from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ResumeHeader, ResumeCategory, ResumeItemShort, ResumeItemLong

class ResumeItemShortInline(admin.TabularInline):
    model = ResumeItemShort
    extra = 0

class ResumeItemLongInline(admin.StackedInline):
    model = ResumeItemLong
    extra = 0

class ResumeCategoryAdmin(admin.ModelAdmin):	
    inlines = [ResumeItemLongInline, ResumeItemShortInline]

admin.site.register(ResumeHeader)
admin.site.register(ResumeCategory, ResumeCategoryAdmin)

