from django.shortcuts import render, redirect
from .models import Board

def home(request):
    savings = Board.objects
    return render(request, 'home.html', {'savings':savings})

def submit(request):
    b = Board()
    b.message = request.GET['message']
    b.writer = request.GET['writer']
    b.pub_date = request.GET['pub_date']
    b.save()
    return redirect('/')
# Create your views here.
