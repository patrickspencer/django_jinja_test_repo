from django.shortcuts import render


def home(request):
    return render(request, 'index.jinja2',
        {'greetings': 'hello world'})

