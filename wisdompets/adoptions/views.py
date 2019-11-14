from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
from  django.http import Http404

def home(request):
    #makek query to fetch all pets
    pets = Pet.objects.all()
    #the render function will pass the responsibility of rendering templates onto html
    #second argument is for the template we want to use
    #the render function makes a dictionary with the data we want to make available
    return render(request, 'home.html', {'pets': pets})

def pet_detail(request, id):
    #returns the string containing the id so we can test the routing
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})
