from django.shortcuts import render	
from django.http import HttpResponse
from .models import blogs
from django.http import HttpResponse
# Create your views here.


def getname(request,):
    name=request.POST.getlist("firstname")
    comment = blogs()
    comment.name = name
    comment.save()
    view=request.POST.getlist("comment")
    comment.comments = view
    comment.save()
    insta = blogs.objects.filter(id__gt=129)
    
  
        
        
    
    
    context = {
    	    'first' : insta,
    	    
    }
    return render(request, 'mycom/second.html',context)
    
def enter(request):
    return render(request, 'mycom/enter.html',{})
    
    
def second(request):
    return render(request, 'mycom/second.html',{})
    
