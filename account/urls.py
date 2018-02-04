from django.urls import path
from .views import views
from .views import signup
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('login',auth_views.login,{"template_name":"account/login.html"},name="login"),
    path('logout',auth_views.logout,{"template_name":"account/logout.html"},name="logout"),
    path('edit',views.edit,name="edit"),
    path('signup',signup.signup,name="signup"),
    path('forget-password',views.forget_password,name="forget_password")
]