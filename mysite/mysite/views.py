from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponse("", 200)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Logged in", status=200)
    else:
        return HttpResponseForbidden("Didnt work")
