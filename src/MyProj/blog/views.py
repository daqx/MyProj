# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from MyProj.blog.models import BlogPost
from django.core.context_processors import request

def archive(request):
    posts=BlogPost.objects.all()
    t=loader.get_template("archive.html")
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))