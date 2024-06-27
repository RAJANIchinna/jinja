from django.shortcuts import render

def condition(request):
    d={'name':'RAJANI','age':3}
    return render(request,'condition.html')

def condition1(request):
    d={'name':'RAJANI','age':35}
    return render(request,'condition1.html')

    
def loop(request):
    d={'name':'RAJANI'}
    return render(request,'loop.html',d)

    