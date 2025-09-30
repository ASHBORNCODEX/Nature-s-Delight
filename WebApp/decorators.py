from django.shortcuts import redirect
from functools import wraps

def session_login_redirect(views_func):
    @wraps(views_func)
    def wrapper(request, *args , **kwargs ):
        if 'Name' not in request.session:
            return redirect('/')
        return views_func(request, *args , **kwargs )
    return wrapper