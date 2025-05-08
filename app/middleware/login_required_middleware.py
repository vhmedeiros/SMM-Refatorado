# # app/middleware/login_required_middleware.py
# from django.shortcuts import redirect
# from django.conf import settings
# import re

# EXEMPT_URLS = [
#     re.compile(settings.LOGIN_URL.lstrip('/')),
#     re.compile(settings.LOGOUT_REDIRECT_URL.lstrip('/')),
#     re.compile(r'^admin/'),  # libera acesso ao /admin/
# ]

# class LoginRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         path = request.path_info.lstrip('/')
        
#         # Se o usuário não está autenticado e a URL não está na lista de exceções
#         if not request.user.is_authenticated:
#             if not any(pattern.match(path) for pattern in EXEMPT_URLS):
#                 return redirect(settings.LOGIN_URL)
        
#         return self.get_response(request)


# app/middleware/login_required_middleware.py
from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse_lazy
import re

EXEMPT_URLS = [
    re.compile(reverse_lazy('login').lstrip('/')),
    re.compile(reverse_lazy('logout').lstrip('/')),
    re.compile(r'^admin/'),
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info.lstrip('/')
        
        if not request.user.is_authenticated:
            if not any(pattern.match(path) for pattern in EXEMPT_URLS):
                return redirect(settings.LOGIN_URL)
        
        return self.get_response(request)
