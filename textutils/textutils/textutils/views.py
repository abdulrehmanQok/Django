from django.http import HttpResponse
def info(request):
    return HttpResponse('''<h1> My name is Abdul Rehman </h1><br><h2>learn from</h2> <a href="https://www.youtube.com/watch?v=AepgWsROO4k">learn more</a>''')