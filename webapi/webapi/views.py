from django.shortcuts import render

def renderhome(request):
    return render(request,'homepage.html')