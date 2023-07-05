from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
# from .models import UserProfile
from django.utils.translation import gettext as _
from django import forms
from .models import Profile
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm

class CustomerRegistrationForm(UserCreationForm):

#   name=forms.CharField(max_length=122,label=("name"))
  first_name = forms.CharField(max_length=30, required=True, help_text='Optional')
  last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
  email = forms.EmailField(max_length=114, help_text='Enter a valid email address')
  #plachholder in django form
  username=forms.CharField(max_length=122,label=("Username"),required=True,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
  class Meta:
      model = User
      fields = [
          'username',
          'first_name',
          'last_name',
          'email',
          'password1',
          'password2',
      ]
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'jobtitle', 'email', 'gitlink', 'linkd', 'number', 'profile', 'skill1', 'skill2', 'skill3', 'technichal1', 'technichal2', 'technichal3', 'technichal4', 'technichal5', 'companyname', 'jobtype', 'sdate', 'edate', 'uname', 'dptname', 'cgpa', 'profile_image']

# class UserForm(forms.ModelForm):
#  class Meta:
#   model = User
#   fields = ['name', 'password', 'email']
		# labels = {,name,: ‘Enter Name’, ‘password’: ‘Enter Password’, ‘email’: ‘Enter Email’ }
		# widgets = {‘password’:forms.PasswordInput} 
		

#   fields = ['name', 'email', 'password']

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

# class UserProfileForm(forms.ModelForm):
#     class Meta:s
#         model = UserProfile
#         fields = ['bio', 'location', 'birth_date']
# class Mychangepassword(PasswordChangeForm):
#     old_password = forms.CharField(label=_ (" Old Password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     new_password1 = forms.CharField(label=_(" NewPassword"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
#     new_password2 = forms.CharField(label=_(" confrom Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'confrom-password','class':'form-control'}))
class Mypasswordreset(PasswordResetForm):
    email=forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))
class Myresetform(SetPasswordForm):
     new_password1 = forms.CharField(label=_(" NewPassword"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
     new_password2 = forms.CharField(label=_(" confrom Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'confrom-password','class':'form-control'}))
