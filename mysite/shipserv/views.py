from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.http import StreamingHttpResponse, HttpResponse, JsonResponse


def check_auth(request, group_name):
    if request.user.is_authenticated:
        if request.user.groups.filter(name=group_name).exists():    
            return True
    return HttpResponseForbidden("<h1>403 Forbidden.</h3><br><h3>You do not have access to this feature.</h3>")
    
def asset_lookup(request):
    is_authenticatd = check_auth(request, "asset_manager")
    if is_authenticatd == True:
        return HttpResponse("Verified")
    else:
        return is_authenticatd


def add_asset(request):
    is_authenticatd = check_auth(request, "asset_manager")
    if is_authenticatd == True:
        return HttpResponse("Verified")
    else:
        return is_authenticatd


def asset_return(request):
    is_authenticatd = check_auth(request, "asset_manager")
    if is_authenticatd == True:
        return HttpResponse("Verified")
    else:
        return is_authenticatd


