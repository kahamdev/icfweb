from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import icf_event,icf_quote,frequent_ask
from .models import faq_qn01,faq_qn02,faq_qn03,faq_qn04




def home(request):
    faqs=frequent_ask.objects.all()
    today=datetime.datetime.now()
    context={
        "today":today,
        "faqs":faqs
    }
    return render(request, 'home.html', context)

def faqs(request):
    faqs=frequent_ask.objects.all()
    context={
        "faqs":faqs
    }
    return render(request, 'faqs.html', context)

def about(request):
    return render(request, 'about.html', {})
    

def contact(request):
    return render(request, 'contact.html', {})

def management(request):
    return render(request, 'management.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def quote(request):
    today=datetime.datetime.now()
    quote=icf_quote.objects.all()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faqs":faqs,
        "quote":quote,
    }
    return render(request, 'quote.html', context)
    
def event(request):
    today=datetime.datetime.now()
    event=icf_event.objects.all()
    faqs=frequent_ask.objects.all()

    context={
        "today":today,
        "event":event,
        "faqs":faqs
    }
    return render(request,'event.html',context)


def question1(request):
    today=datetime.datetime.now()
    faq01=faq_qn01.objects.all()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faq01":faq01,
        "faqs":faqs
    }
    return render(request,'question-one.html',context)


def question2(request):
    today=datetime.datetime.now()
    faq02=faq_qn02.objects.all()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faq02":faq02,
        "faqs":faqs
    }
    return render(request,'question-two.html',context)


def question3(request):
    today=datetime.datetime.now()
    faq03=faq_qn03.objects.all()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faq03":faq03,
        "faqs":faqs
    }
    return render(request,'question-three.html',context)


def question4(request):
    today=datetime.datetime.now()
    faq04=faq_qn04.objects.all()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faq04":faq04,
        "faqs":faqs
    }
    return render(request,'question-four.html',context)


def wudhu(request):
    today=datetime.datetime.now()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faqs":faqs
    }
    return render(request,'wudhu.html',context)

def zakat(request):
    today=datetime.datetime.now()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faqs":faqs
    }
    return render(request,'zakat.html',context)

def salat(request):
    today=datetime.datetime.now()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faqs":faqs
    }
    return render(request,'salat.html',context)

def fasting(request):
    today=datetime.datetime.now()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faqs":faqs
    }
    return render(request,'fastingRamadan.html',context)

def hijah(request):
    today=datetime.datetime.now()
    faqs=frequent_ask.objects.all()
    context={
        "today":today,
        "faqs":faqs
    }
    return render(request,'hijah.html',context)

def donate(request):
    context={}
    return render(request,'donate.html',context)
    