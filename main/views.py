from django.shortcuts import render

from .models import CollegeContactModel, CollegePartnersModel
from news.models import NewsModel
from specialties.models import SpecInfoModel


def index(request):
    last_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[1:4]
    achivments = NewsModel.objects.filter(news_is_achivment = True).order_by('news_create_date')[:4]
    contacts = CollegeContactModel.objects.all()
    partners = CollegePartnersModel.objects.all()
    
    last_one_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[0]

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