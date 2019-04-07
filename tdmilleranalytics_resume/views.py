from django.shortcuts import render
from django.http import HttpResponse
from .models import ResumeHeader, ResumeCategory

# Create your views here.


def index(request):
    resume_header_list = ResumeHeader.objects.all()
    resume_category_list = ResumeCategory.objects.all()
    resume_category_ids_long = [x.id for x in resume_category_list if (x.resumeitemlong_set.all().count() > 0)]
    resume_category_ids_short = [x.id for x in resume_category_list if (x.resumeitemlong_set.all().count() == 0)]
    resume_category_list_long = ResumeCategory.objects.filter(id__in=resume_category_ids_long)
    resume_category_list_short = ResumeCategory.objects.filter(id__in=resume_category_ids_short)
    context = {'resume_header_list': resume_header_list, 'resume_category_list_long': resume_category_list_long, 'resume_category_list_short': resume_category_list_short}
    return render(request, 'tdmilleranalytics_resume/index.html', context)
