from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
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
            wheel = form.save(commit=False)
            wheel.created_by = request.user
            wheel.save()
            form.save_m2m()
            for n in range(wheel.numSegments):
                prizename = "Prize"
                if n % 2:
                    prizename = "Win " + str(n+1)
                    segment = Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk), name=prizename, fillStyle="#ffffff", textFillStyle="#000000")
                else:
                    prizename = "Lose " + str(n+1)
                    segment = Segment.objects.create(wheel=Wheel.objects.get(pk=wheel.pk), name=prizename, fillStyle="#000000", textFillStyle="#ffffff")
            return redirect('main:wheeldetail',pk=wheel.pk)
    else:
        form = WheelForm
        return render(request, 'main/wheel_form.html', {'form':form})

def wheeldetail(request, pk):
    wheel = get_object_or_404(Wheel, pk=pk)
    return render(request, 'main/wheeldetail.html', {'wheel':wheel})

def wheel_public_view(request, pk):
    wheel = get_object_or_404(Wheel, pk=pk)
    return render(request, 'main/wheel_public.html', {'wheel':wheel})

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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome, {username}")
            login(request, user)
            return redirect('main:wheel_list')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]}")

            return render(request, "main/register_form.html", {"form":form})
    else:
        form = UserCreationForm
        return render(request, 'main/register_form.html', {'form':form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome {username}")
                return redirect('main:wheel_list')
            else:
                messages.error(request, "Username and password did not work")
        else:
            messages.error(request,"Login is not valid")
    
    form = AuthenticationForm()
    return render(request, 'main/login_form.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.info(request, "Logged out success")
    return redirect('main:wheel_list')

