from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
class IndexView(View):
    """
    the initial generic view for the project. Will eventually have login
    abilities
    """

    def get(self, request):
        return HttpResponse('Welcome to leXicology!\nThis needs a '
                            'template...')