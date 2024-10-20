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
    
    # Punctuation symbols to be removed
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    analyzed = ""  # Initialize as an empty string instead of having a space
    
    if removepunc == 'on':  # Make sure this check is performed
        for char in djtext:
            if char not in punctuations:
                analyzed += char
    
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        
        return render(request, 'analyze.html', params)
    
    # Handle the case when 'removepunc' is not selected (optional)
    else:
        return HttpResponse("Error: Remove punctuation option is not selected.")



# def capitalizefirst(request):
#     return HttpResponse ('''<h1> capitalize first</h1> <a href="http://127.0.0.1:8000/"> <button> capitalize first</button> </a>''')

# def removespace(request):
#     return HttpResponse ("<h1> remove space </h1>")

# def charcounter(request):
#     return HttpResponse ("<h1> char counter </h1>")

# def newlineremove(request):
#     return HttpResponse ("<h1> new line remove </h1>")