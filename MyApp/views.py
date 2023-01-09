from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable": "This is sent"
    }
    return render(request, 'index.html', context)

   # return HttpResponse('This is HomePage')

def about(request):
    return HttpResponse('This is About Page')

def services(request):
    return HttpResponse('This is Services Page')

def contact(request):
    return HttpResponse('This is Contact Page')

