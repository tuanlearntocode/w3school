from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Q

from members.models import Members


# Create your views here.
def members(request):
    mymembers = Members.objects.all().values() 
    template = loader.get_template("all_members.html")
    context = {
        "mymembers" : mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember" : mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    mymembers = Members.objects.all()
    template = loader.get_template("template.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))


def testing2(request):
    mydata = Members.objects.all().order_by("lastname", "-id")
    template = loader.get_template("template.html")
    context = {
        "mymembers" : mydata,
    }
    return HttpResponse(template.render(context, request))