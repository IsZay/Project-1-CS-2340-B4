from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    # return HttpResponse("Hello, world. You're at the index.")
    return render(request, 'home/index.html', {'template_data': template_data})
def about(request):
    return render(request, 'home/about.html')