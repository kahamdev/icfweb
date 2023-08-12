from django.urls import path
from . import views

# we add some url for video media
from django.conf.urls.static import static
from django.conf import settings



# Other urls
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('management/',views.management, name='management'),
    path('gallery/',views.gallery, name='gallery'),
    path('quote/',views.quote,name='quote'),
    path('event/',views.event,name='event'),
    path('question-one/',views.question1,name='question-one'),
    path('question-two/',views.question2,name='question-two'),
    path('question-three/',views.question3,name='question-three'),
    path('question-four/',views.question4,name='question-four'),
    path('wudhu/',views.wudhu, name='wudhu'),
    path('salat/',views.salat, name='salat'),
    path('fasting/',views.fasting, name='fasting'),
    path('hijah/',views.hijah, name='hijah'),
    path('zakat/',views.zakat, name='zakat'),
    path('donate/',views.donate, name='donate'),
]

urlpatterns += static (settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

