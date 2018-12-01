from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def translate(request):
    original = request.GET['originaltext']

    translation = ''
    for word in original.split():
        if word[0] in ['a','e','i','o','u']:
            # Vowel
            translation += word
            translation += 'vowel'
        else:
            # consonant
            # heese
            translation += word[1:]
            # c
            translation += word[0]
            # ay
            translation += 'ay '
            translation += word
            translation += 'consonant'
    return render(request,'translate.html', {'original':original,'translation':translation})

def about(request):
    return render(request,'about.html')