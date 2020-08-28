from django.shortcuts import render
import requests
import sys
import subprocess


def button(request):

    return render(request,'Product Finder.html')

def output(request):
    data=requests.get("https://google.com")
    print(data.text)
    data=data.text
    return render(request,'Product Finder.html',{'data':data})

def external(request):
    inp=request.POST.get('param')
    out=subprocess.run([sys.executable,"E:\\unityprojects\\github\\pdsearch\\pd\\external.py",inp],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(out)
    out=out.stdout
    return render(request,'Product Finder.html',{'data':out.decode('utf-8')})
    #return render(request,'Product Finder.html',{'data1':out.stdout})
    #return render(request,'Product Finder.html',{'data1':out.stdout.decode('utf-8')})