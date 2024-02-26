from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from movieapp.models import Movie
def detail(request,id):

    data = Movie.objects.get(pk=id)
    context = {
        "Movies":data
    }
    return render(request,"details.html",context)

# Create your views here.
def print_hello(request):
    # return HttpResponse("Hellooo")
    #  movie_list={
    #      'tittle':'premalu',
    #     'year':2024,
    # #     'description':'A mlayalam movie',
    # # }
    data = Movie.objects.all()
    context= {
        'Moviess':data
        

    }
    
    data = Movie.objects.all()
    print(data)

    # return HttpResponse("String")
    return render(request,'hello.html',context)

def index(request):
    return render(request,'index.html')

def add(request):
    tittle = request.POST.get('tittle')
    year = request.POST.get('year')
    description = request.POST.get('description')
    if tittle and year and description:
        movie=Movie(tittle=tittle, year=year, description=description)
        movie.save()
        return HttpResponseRedirect('/hello')
    return render(request,'add.html')

def delete(request,id):
    try:
        data = Movie.objects.get(pk=id)
        print(data)
    except:
        raise Http404("Does not exist")
    data.delete()
    return HttpResponseRedirect('/hello')
    
   
