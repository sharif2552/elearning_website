# decorators.py

from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponse

def student_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated and has the student role
        if request.user.is_authenticated and request.user.user_type == 'student':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("you need to be a student to give exam")  # Redirect to login page or other appropriate page
    return _wrapped_view



from functools import wraps
from django.http import HttpResponseForbidden

def teacher_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'teacher':

            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Permission denied.")
    return _wrapped_view
