from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from .forms import MovieForm

# Create your views here.
def index(request):
    obj=movie.objects.all()
    return render(request,'index.html',{'movie_list':obj})

# def id(request,movie_id):
#     return HttpResponse('movie id is %s' % movie_id)

def link(request):
    obj = movie.objects.all()
    return render(request,'id.html',{'movie_list':obj})

def details(request,movie_id):
    x=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':x})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']

        movie_add=movie(name=name,desc=desc,year=year,img=img)
        movie_add.save()

    return render(request,'add.html')

def edit(request,id):
    movie1=movie.objects.get(id=id)
    form1=MovieForm(request.POST or None, request.FILES, instance=movie1)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form1, 'movie':movie1})

def delete(request,id):
    if request.method=='POST':
        x = movie.objects.get(id=id)
        x.delete()
        return redirect('/')
    return render(request,'delete.html')