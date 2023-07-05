"""crispyform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
from home import forms
from django.conf import settings
from django.conf.urls.static import static
from crispyform.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from home.forms import Mypasswordreset,Myresetform
urlpatterns = [
    path('create_profile', views.create_profile, name='create_profile'),
    path('admin/', admin.site.urls),
    path('profile',views.profile,name="profile"),
    path('',auth_views.LoginView.as_view(template_name='login.html',authentication_form=forms.LoginForm),name="login"),
    path('register/',views. CustomerRegisterView.as_view(),name="customerregistration"),
    path("logout/",auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    path('<int:id>/',views.resume,name="resume"),
    path('profile/list/',views.list,name='list'),
    #path('contact/',views.contact,name="contact"),
    
    path('password-reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=Mypasswordreset),name="password-reset"),
    path('password-reset-done',auth_views.PasswordResetDoneView.as_view(template_name='password_done.html'),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=Myresetform),name="password_reset_confirm"),
   #path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html',form_class=Myresetform), name='reset_password_confirm')
   path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
