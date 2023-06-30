from django.shortcuts import render

from .models import CollegeContactModel, CollegePartnersModel
from news.models import NewsModel
from specialties.models import SpecInfoModel


def index(request):
    last_news = NewsModel.objects.filter(news_is_published = True).order_by('news_create_date')[:3]
    achivments = NewsModel.objects.filter(news_is_achivment = True).order_by('news_create_date')[:4]
    contacts = CollegeContactModel.objects.all()
    partners = CollegePartnersModel.objects.all()

    context = {
        'last_news': last_news,
        'contacts' : contacts,
        'partners' : partners,
        'achivments' : achivments,
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