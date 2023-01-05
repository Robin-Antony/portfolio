from django.shortcuts import render

# Create your views here.
def register_page(request):
    return render(request,'accounts/register.html')


def login_page(request):
    return render(request,'accounts/login.html')