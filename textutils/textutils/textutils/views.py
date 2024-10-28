from django.http import HttpResponse
from django.shortcuts import render
def info(request):
    info = {
        'name':'Abdul Rehman',
        'course':'html',
        'link':'https://www.youtube.com/watch?v=AepgWsROO4k'
    }
  
    return render(request, 'index.html',info)


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    spaceremover=request.POST.get('spaceremover','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""  
    
    if removepunc == "on":  
        for char in djtext:
            if char not in punctuations:
                analyzed += char
    
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremove=="on":
        analyzed=""
        for char in djtext:
            if char!= "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        
        djtext=analyzed
    if spaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]=="  "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        djtext=analyzed
    if(removepunc!="on" and fullcaps!="on" and newlineremove!="on" and spaceremover!="on"):
        return HttpResponse("Error: No operation selected")
    return render(request, 'analyze.html', params)
 