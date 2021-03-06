# from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import loader
# from .forms import *
from .models import *
# from .filters import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def index(request):
	videoJenna = Video.objects.filter(tags__contains='homepage', tags__icontains='jenna')
	videoJacquie = Video.objects.filter(tags__contains='homepage', tags__icontains='jacquie')
	videoEric = Video.objects.filter(tags__contains='homepage', tags__icontains='eric')
	videoDemo = Video.objects.filter(tags__contains='homepage', tags__icontains='demo')
	return render(request,'homepage.html', {'videoJenna' : videoJenna, 'videoJacquie' : videoJacquie, 'videoEric' : videoEric, 'videoDemo' : videoDemo, }) 

def twopage(request):
	return render(request,'home.html') 

def sitetheme(request):
	return render(request,'FAL_Theme.html') 