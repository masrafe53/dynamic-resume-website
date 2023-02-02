from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import (
    Services,RecentWork,Clint,MySelf,Blog
)
from django.views.generic import DateDetailView
from django.views import generic
# Create your views here.
def home(request):
    services = Services.objects.all
    recentwork = RecentWork.objects.all
    clint = Clint.objects.all
    myself = MySelf.objects.all
    my_dic = {"services":services,"recentwork":recentwork,
    "clint":clint,"myself":myself}
    return render(request,'index.html',context=my_dic)

def blog(request):
    blog = Blog.objects.all
    dic = {"blog":blog}
    return render(request,'blog.html',context=dic)

def work(request,id):
    work = get_object_or_404(RecentWork, id = id)
    dic = {"work":work}
    return render(request,'work.html',context=dic)

def service(request,id):
    service = get_object_or_404(Services,id = id)
    my_dic = {"service":service}
    return render(request,'service.html',context=my_dic)