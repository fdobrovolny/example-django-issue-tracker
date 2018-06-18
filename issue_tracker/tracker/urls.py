from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('accounts/login', auth_views.login,
         {'template_name': 'tracker/signin.html'}, name='login'
         ),
    path('accounts/logout', auth_views.logout,
         {'next_page': '/accounts/login?logout=1'}, name='logout'
         ),
]