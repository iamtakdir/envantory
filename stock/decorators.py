from django import http
from django.contrib.auth import decorators
from django.http import HttpResponse
from django.http.request import validate_host
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args,**kwargs):

            group = None

            if request.user.groups.exists():
                group= request.user.groups.all()[0].name

            if group in allowed_roles:
                
                return view_func(request, *args,**kwargs)
            else:
                return HttpResponse ("<h1> You are not authorized to delete Stock , ask Admin </h1>")
        return wrapper_func
    return decorator