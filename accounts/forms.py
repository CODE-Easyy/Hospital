from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate, login

from .models import Doctor
from hospitals.models import Hospital


class RegistrationForm(forms.ModelForm):
	working_place = forms.ModelChoiceField(queryset = Hospital.objects.all())
	password = forms.CharField(label = 'Password', widget = forms.PasswordInput)

	class Meta:
		model = Doctor
		fields = ('email', 'name', 'lastname', 'phone', 'working_place', 'role', 'picture', 'password')

	def save(self, commit = True):


		user = super().save(commit = False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user





class UserCreationForm(forms.ModelForm):
	working_place = forms.ModelChoiceField(queryset = Hospital.objects.all())
	password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'PasswordConfirmation', widget = forms.PasswordInput)


	class Meta:
		model = Doctor
		fields = ('email', 'name', 'lastname', 'phone', 'working_place', 'role', 'picture', 'is_staff', 'is_superuser')

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")


		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit = True):
		user = super().save(commit = False)
		user.set_password(self.cleaned_data["password1"])

		if commit:
			user.save()
		return user



class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = Doctor
		fields = ('email', 'name', 'phone', 'picture', 'password', 'is_active', 'is_superuser')

	def clean_password():
		return self.inital["password"]