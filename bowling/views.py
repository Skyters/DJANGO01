from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from bowling.models import Client

# Create your views here.
class ShowBowlingView(View):
    def get(request, *args, **kwargs):
        clients = Client.objects.all()

        result = ""
        for s in clients:
            result += s.name + "<b>"

        return HttpResponse(result)