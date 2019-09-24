from django.shortcuts import render, redirect, get_object_or_404
from .models import Wheel, Segment, Animation
from .forms import WheelForm

def homepage(request):
    return render(request, 'main/home.html',{})

def wheelfortune(request):
    return render(request, 'main/wheelfortune.html',{})

def wheelcreate(request):
    if request.method == "POST":
        form = WheelForm(request.POST)
        if form.is_valid():
            wheel = form.save()
            return redirect('main:wheeldetail',pk=wheel.pk)
    else:
        form = WheelForm
        return render(request, 'main/wheelcreate.html', {'form':form})

def wheeldetail(request, pk):
    wheel = get_object_or_404(Wheel, pk=pk)
    return render(request, 'main/wheeldetail.html', {'wheel':wheel})

def wheeledit(request,pk):
    wheel = get_object_or_404(Wheel, pk=pk)
    if request.method == "POST":
        form = WheelForm(request.POST)
        if form.is_valid():
            wheel = form.save()
            return redirect('main:wheeldetail', pk=wheel.pk)
    else:
        form = WheelForm(instance=wheel)
        return render(request, 'main/wheeledit.html', {'form':form})

def wheel_list(request):
    wheel_list = Wheel.objects.all()
    return render(request, 'main/wheel_list.html', {'wheel_list':wheel_list})