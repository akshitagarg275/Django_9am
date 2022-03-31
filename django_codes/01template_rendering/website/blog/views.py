from django.shortcuts import render

# Create your views here.


def home(request):
    user = "John Doe"
    data = {
        "user": user
    }
    return render(request, 'home.html',data)


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")