from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghigklmnopqrstuwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTUWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    len = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(len):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def info(request):
    return render(request, 'generator/info.html')
