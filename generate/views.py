from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generate/home.html')

def about(request):
    return render(request, 'generate/about.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    # a list named characters which contains the lowercase letters

    if request.GET.get('uppercase'): 
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        # if uppercase checkbox is checked, uppercase letters are included in characters list
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
        # if special character checkbox is checked, special letters are included in characters list 
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
        # if numbers checkbox is checked, numbers  are included in characters list

    length = int(request.GET.get('length',12)) 
    # gets the desired length for password; default is 12

    thepassword = '' #set the password to an empty string
    for x in range(length):
        thepassword += random.choice(characters)
        #loops through the characters list and inserts a random character to the password

    return render(request, 'generate/password.html', {'password':thepassword}) 
    # returns the password to the password.html page
