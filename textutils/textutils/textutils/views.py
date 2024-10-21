from django.http import HttpResponse
from django.shortcuts import render
def info(request):
    # return HttpResponse('''<h1> My name is Abdul Rehman </h1><br><h2>learn from</h2> <a href="https://www.youtube.com/watch?v=AepgWsROO4k">learn more</a>''')
    info = {
        'name':'Abdul Rehman',
        'course':'html',
        'link':'https://www.youtube.com/watch?v=AepgWsROO4k'
    }
  
    return render(request, 'index.html',info)

#pipeline
def analyze(request):
    # Use request.GET.get instead of request.Get.get
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremove=request.GET.get('newlineremove','off')
    spaceremover=request.GET.get('spaceremover','off')
    # Punctuation symbols to be removed
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    analyzed = ""  # Initialize as an empty string instead of having a space
    
    if removepunc == "on":  # Make sure this check is performed
        for char in djtext:
            if char not in punctuations:
                analyzed += char
    
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        
        return render(request, 'analyze.html', params)
    
    # Handle the case when 'removepunc' is not selected (optional)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        
        return render(request, 'analyze.html', params)
    elif newlineremove=="on":
        analyzed=""
        for char in djtext:
            if char!= "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        
        return render(request, 'analyze.html', params)
    elif spaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]=="  "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")



# def capitalizefirst(request):
#     return HttpResponse ('''<h1> capitalize first</h1> <a href="http://127.0.0.1:8000/"> <button> capitalize first</button> </a>''')

# def removespace(request):
#     return HttpResponse ("<h1> remove space </h1>")

# def charcounter(request):
#     return HttpResponse ("<h1> char counter </h1>")

# def newlineremove(request):
#     return HttpResponse ("<h1> new line remove </h1>")