from django.shortcuts import render

def index(request):
    return render(request, 'stability/index.html')
