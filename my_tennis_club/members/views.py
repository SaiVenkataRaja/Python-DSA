# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):               #This is a simple example on how to send a response back to the browser.
#     return HttpResponse("Hello World !")

from django.shortcuts import render

def members(request):
    return render(request, 'members/home.html')
