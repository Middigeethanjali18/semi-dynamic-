from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'geetha'}
    return render(request,'wish.html',context=d)

def conditions(request):
    d={'age':21}
    return render(request,'conditions.html',context=d)

def conditions(request):
    d={'a':10,'b':20}
    return render(request,'conditions.html',context=d)


def conditions(request):
    d={'a':10,'b':50,'c':300}
    return render(request,'conditions.html',d)


def loop(request):
    d={'name':''}
    return render(request,'loop.html',d)