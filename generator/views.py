from django.shortcuts import render
import random
import string


def home(request):
    return render(request, 'generator/home.html', {'title': 'Password Generator'})


def password(request):
    characters = string.ascii_lowercase

    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase

    if request.GET.get('special'):
        characters += string.punctuation

    if request.GET.get('numbers'):
        characters += string.digits
    length = int(request.GET.get('length', 12))

    the_password = ''.join(random.choices(characters, k=length))

    return render(request, 'generator/password.html', {'password': the_password, 'title': 'Ready Password'})
