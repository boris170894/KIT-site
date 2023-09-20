from django.shortcuts import render

from .models import (
                        CollegeContactModel, 
                        CollegePartnersModel, 
                        CollegeHistoryModel, 
                        CollegeDocsModel
                     )
from news.models import NewsModel
from specialties.models import SpecInfoModel


def index(request):
    public__news_count = NewsModel.objects.filter(news_is_published = True).count()
    last_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[public__news_count-4:public__news_count-1]
    achivments = NewsModel.objects.filter(news_is_published = True, news_is_achivment = True).order_by('-news_create_date')[:3]
    
    contacts = CollegeContactModel.objects.all()
    partners = CollegePartnersModel.objects.all()
    
    last_one_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[public__news_count-1]

    context = {
        'last_news': last_news,
        'contacts' : contacts,
        'partners' : partners,
        'achivments' : achivments,
        
        'last_one_news': last_one_news,
    }
    return render(request, 'main/pages/index.html', context)

def applicants(request):
    
    specs = SpecInfoModel.objects.all()
    contacts = CollegeContactModel.objects.all()

    context = {
        'specs' : specs,
        'contacts' : contacts,
    }

    return render(request, 'main/pages/applicants.html', context)

def college_history(request):
    histories = CollegeHistoryModel.objects.all().order_by('year')
    
    context = {
        'histories': histories
    }
    return render(request, 'main/pages/about/history.html', context)

def documents(request):
    documents = CollegeDocsModel.objects.last()
    
    context = {
        'documents': documents
    }
    return render(request, 'main/pages/about/documents.html', context)
