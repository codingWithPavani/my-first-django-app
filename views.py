
from django.http import HttpResponse

def home(request):
    return HttpResponse("👋 Hey! It's my first Django project 😊")
