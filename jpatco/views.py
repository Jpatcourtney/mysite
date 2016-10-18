from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'jpatco/home.html')

def collection(request):
    return render(request, 'jpatco/collection.html')

def redirecthome(request):
    return redirect('home')