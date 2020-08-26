from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE


def button(request):

    return render(request,'Product Finder.html')

def output(request):
    data=requests.get("https://google.com")
    print(data.text)
    data=data.text
    return render(request,'Product Finder.html',{'data':data})

def external(request):
    inp=request.POST.get('param')
    out=run([sys.executable,'//mnt//c//Users//howto//pd//external.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'Product Finder.html',{'data1':out.stdout})