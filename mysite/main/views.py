from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Wheel, Segment, Animation
from .forms import WheelForm, SegmentForm

def homepage(request):
    return render(request, 'main/home.html',{})

def wheelfortune(request):
    return render(request, 'main/wheelfortune.html',{})

def wheelcreate(request):
    if request.method == "POST":
        form = WheelForm(request.POST)
        if form.is_valid():
            wheel = form.save()
            for n in range(wheel.numSegments):
                if n % 2:
                    segment = Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk), name="Prize", fillStyle="#ffffff", textFillStyle="#000000")
                else:
                    segment = Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk), name="Prize", fillStyle="#000000", textFillStyle="#ffffff")
            return redirect('main:wheeldetail',pk=wheel.pk)
    else:
        form = WheelForm
        return render(request, 'main/wheel_form.html', {'form':form})

def wheeldetail(request, pk):
    wheel = get_object_or_404(Wheel, pk=pk)
    return render(request, 'main/wheeldetail.html', {'wheel':wheel})

def wheeledit(request,pk):
    wheel = get_object_or_404(Wheel, pk=pk)
    if request.method == "POST":
        form = WheelForm(request.POST, instance=wheel)
        if form.is_valid():
            wheel = form.save()
            return redirect('main:wheeldetail', pk=wheel.pk)
    else:
        form = WheelForm(instance=wheel)
        return render(request, 'main/wheeledit_form.html', {'form':form})

def wheel_list(request):
    wheel_list = Wheel.objects.all()
    return render(request, 'main/wheel_list.html', {'wheel_list':wheel_list})

def edit_segment(request,pk):
  # TODO: accept wheel pk as lookup to segment fk. Save new segments with wheel pk as fk
  # check for existing segments and pass them as context to template
    current_segment = get_object_or_404(Segment, pk=pk) # check for valid Wheel
    if request.method == "POST":
        form = SegmentForm(request.POST, instance=current_segment)
        if form.is_valid():
            current_segment = form.save()
            return redirect('main:wheeldetail', pk=current_segment.wheel_id)
    else:
        form = SegmentForm(instance=current_segment)
        return render(request, 'main/segment_form.html', {'form':form})

def add_segment(request,pk):
    current_wheel = get_object_or_404(Wheel, pk=pk)
    pass