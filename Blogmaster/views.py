from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
import requests
url1 = "https://www.amazon.in/Apple-iPhone-14-128GB-Starlight/dp/B0BDK8LKPJ/ref=sr_1_1_sspa?crid=3NNPD16QHEMXP&keywords=iphone+14&qid=1663508855&sprefix=iphone+14+%2Caps%2C235&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQ001QlZPT1Q2VjFNJmVuY3J5cHRlZElkPUEwNDYxNzk5M0JZSk81SldIVUVGMyZlbmNyeXB0ZWRBZElkPUEwNDAxMjc2MURBVTdUUkZQVjhBVyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

# Create your views here.

def home(request):
     return render(request,'home.html')

def news(request):
     return render(request,'news.html')

def reviews(request):
     return render(request,'reviews.html')

def phonefinder(request):
     return render(request,'phonefinder.html')

def Evs(request):
     return render(request,'Evs.html')

def compare(request):
     return render(request,'compare.html')

def aboutus(request):
     return render(request,'aboutus.html')

def Contactus(request):
     return render(request,'Contactus.html')

def termsandcondition(request):
     return render(request,'terms.html')

def privacypolicy(request):
     return render(request,'privacy.html')

def review1(request):
     return render(request,'reviews/review1.html')

def review2(request):
     return render(request,'reviews/review2.html')

def news1(request):
     return render(request,'news/news1.html')

def news2(request):
     return render(request,'news/news2.html')

def news3(request):
     return render(request,'news/news3.html')