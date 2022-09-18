from Blogmaster import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name='home'),
    path("news",views.news,name='news'),
    path("reviews",views.reviews,name='reviews'),
    path("phonefinder",views.phonefinder,name='phonefinder'),
    path("Evs",views.Evs,name='Evs'),
    path("compare",views.compare,name='compare'),
    path("aboutus",views.aboutus,name='aboutus'),
    path("Contactus",views.Contactus,name='Contactus'),
    path("termsandcondition",views.termsandcondition,name='termsandcondition'),
    path("privacypolicy",views.privacypolicy,name='privacypolicy'),
    path("review1",views.review1,name='review1'),
    path("review2",views.review2,name='review2'),
    path("news1",views.news1,name='news1'),
    path("news2",views.news2,name='news2'),
    path("news3",views.news3,name='news3'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)