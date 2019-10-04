from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(*args , **kwargs):
    return HttpResponse("<h1>hello world! home page</h1>")

def about(request):
    return render(request, "blog/about.html" , {})

def contact(request):
    return HttpResponse("<h1>hello world ! contact page</h1>")

def post_list(request):
    return render(request, 'blog/post_list.html', {})
