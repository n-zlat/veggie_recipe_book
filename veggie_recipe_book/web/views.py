from django.shortcuts import render


def get_profile():
    return 'hey'


def index(request):
    return render(request, 'base.html')

