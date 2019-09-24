from django.shortcuts import render

def homepage(request):
    return render(request, 'main/home.html',{})

def wheelfortune(request):
    return render(request, 'main/wheelfortune.html',{})
