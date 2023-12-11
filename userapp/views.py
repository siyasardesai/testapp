from django.shortcuts import render,HttpResponse
from django.template import loader
from .models import UserDetails

# Create your views here.
def html_page(request):
    return render(request,"index.html")

def members(request):
    myusers=UserDetails.objects.all().values()
    template=loader.get_template("all_users.html")
    context={
        'myusers':myusers,
    }
    return HttpResponse(template.render(context,request))