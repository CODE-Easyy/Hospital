from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate, login

from .models import Doctor
from hospitals.models import Hospital


class RegistrationForm(forms.ModelForm):
	name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Имя'}))
	lastname = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Фамилия'}))
	working_place = forms.ModelChoiceField(queryset=Hospital.objects.all(), widget = forms.Select(attrs = {'class': 'form-control', 'placeholder': 'Лечебное учреждение'}))
	role = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Должность'}))
	phone = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Номер телефона'}))
	email = forms.EmailField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Электронный адрес'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Пароль'}))
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Введите еще раз'}))

	class Meta:
		model = Doctor
		fields = ('email', 'name', 'lastname', 'phone', 'working_place', 'role', 'picture', 'password')

	def save(self, commit = True):
		user = super().save(commit = False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2





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
		fields = ('email', 'name','lastname', 'phone','working_place','role', 'picture', 'password', 'is_active', 'is_superuser', 'is_accept')

	def clean_password(self):
		return self.initial["password"]




class UserLoginForm(forms.Form):
    email = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Email...'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Password...'}))


    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email = email, password = password)
            if not user:
                raise forms.ValidationError('Такого пользователя нет')
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')

        return super(UserLoginForm, self).clean(*args, **kwargs)



class ProfileUpdate(forms.ModelForm):
	class Meta:
		model = Doctor
		fields = ('email', 'phone')
