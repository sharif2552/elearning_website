# # decorators.py

# from functools import wraps
# from django.shortcuts import redirect

# def student_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         # Check if the user is authenticated and has the student role
#         if request.user.is_authenticated and request.user.Profile.user_type == 'student':
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('login')  # Redirect to login page or other appropriate page
#     return _wrapped_view



# def teacher_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         # Check if the user is authenticated and has the teacher role
#         if request.user.is_authenticated and request.user.profile.user_type == 'teacher':
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('login')  # Redirect to login page or other appropriate page
#     return _wrapped_view