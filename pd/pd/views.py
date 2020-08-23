from django.shortcuts import render
import requests


def button(request):

    return render(request,'Product Finder.html')

def output(request):
    data=requests.get("https://google.com")
    print(data.text)
    data=data.text
    return render(request,'Product Finder.html',{'data':data})