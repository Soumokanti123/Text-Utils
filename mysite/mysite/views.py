# I have created this file - soumo
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def index2(request):
    return render(request, "index2.html")
def about(request):
    return render(request,"about.html")

def navigate2(request):
    return render(request,"navigate2.html")
def navigate(request):
    return render(request,"navigate.html")
def analyze(request):

    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    fullcap = request.POST.get('fullcap','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charCounter = request.POST.get('charCounter', 'off')

    if removepunc == 'on':
        punctuation = '''/[-[\]{}()*+?.,;:''\\%@^$|#\]/g""\\$&'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed+= char
        params = {'purpose':'Remove Puntuations','analyzed_text':analyzed}
        djtext = analyzed

    if fullcap == 'on':
        analyzed = ""
        for char in djtext:
            analyzed= analyzed+char.upper()
        params = {'purpose':'Upper Cases','analyzed_text':analyzed}
        djtext = analyzed
            # return render(request,'analyze.html',params)

    if newlineremover=='on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char !="\r":
                analyzed += char
        params = {'purpose': 'Removed New line', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover=='on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed+=char
        params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}
        djtext = analyzed


    if charCounter=='on':
        analyzed = 0
        for char in djtext:
            if char != ' ':
                analyzed += 1
        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}

    if removepunc!="on" and  fullcap!="on" and newlineremover!="on" and spaceremover!="on" and charCounter!="on":
        return HttpResponse("Please Rewrite Your Text...")

    return render(request, 'analyze.html', params)
