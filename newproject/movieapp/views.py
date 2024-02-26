from django.shortcuts import render
from django.http import HttpResponse
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

