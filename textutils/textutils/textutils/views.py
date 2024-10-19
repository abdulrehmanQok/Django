from django.http import HttpResponse
def info(request):
    return HttpResponse('''<h1> My name is Abdul Rehman </h1><br><h2>learn from</h2> <a href="https://www.youtube.com/watch?v=AepgWsROO4k">learn more</a>''')

#pipeline
def removepunc(request):
    return HttpResponse ('''<h1> remove punc </h1> <a href="http://127.0.0.1:8000/"> <button> backhome page</button> </a>''')

def capitalizefirst(request):
    return HttpResponse ('''<h1> capitalize first</h1> <a href="http://127.0.0.1:8000/"> <button> capitalize first</button> </a>''')

def removespace(request):
    return HttpResponse ("<h1> remove space </h1>")

def charcounter(request):
    return HttpResponse ("<h1> char counter </h1>")

def newlineremove(request):
    return HttpResponse ("<h1> new line remove </h1>")