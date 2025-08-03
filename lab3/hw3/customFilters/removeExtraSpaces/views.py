# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def example_view(request):
    text = "This    is   an   example    with   extra   spaces."
    context = {
        'text': text,
        'json':{
            "name": "Ziad",
            "skills": ["Python", "Django"],
            "info": {
                "age": 25,
                "city": "Sana'a"
            }
        }
    }
    return render(request, 'customFilter.html',context)

