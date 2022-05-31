from django.shortcuts import render
from .models import Models
from django.forms import SlugField
from django.http import HttpResponse,JsonResponse


# Create your views here.
def index(request):
    models = Models.objects.all()
    print(models)
    context ={'models':models}
    return render(request,'blogApp/index.html', context)
def detail(request, pk):
    models = Models.objects.get(slug=pk)   
    context ={'models':models} 
    return render(request, 'blogApp/detail.html', context)




