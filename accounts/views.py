from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import Doctor
from .forms import RegistrationForm, UserLoginForm



class RegistrationView(CreateView):
	template_name = 'accounts/register.html'
	form_class = RegistrationForm


	def get_context_data(self, *args, **kwargs):
		context = super(RegistrationView, self).get_context_data(*args, **kwargs)
		context['next'] = self.request.GET.get('next')
		return context


	def get_success_url(self):
		next_url = self.request.POST.get('next')
		success_url = reverse('login')

		if next_url:
			success_url += '?next = {}'.format(next_url)
		return success_url



def login_page(request):
	form = UserLoginForm(request.POST or None)
	next_ = request.GET.get('next')

	if form.is_valid():
		email = request.POST.get('email')
		password = request.POST.get('password')

		try:
			temp_user = Doctor.objects.get(email = email)
			if temp_user.is_accept:
				user = authenticate(email = email.strip(), password = password.strip())

				login(request, user)
				next_post = request.POST.get('next')
				redirect_path = next_ or next_post or '/'

				return redirect(redirect_path)
			else:
				context = {'form':form, 'error': 'ALMAZ KOTAK'}
				return render(request, 'accounts/login.html', context)

		except Doctor.DoesNotExist:
			pass



	return render(request, 'accounts/login.html', {'form':form})


class ProfileView(UpdateView):
	model = Doctor
	fields = ['name','lastname', 'phone','working_place','role', 'picture']
	template_name = 'accounts/profile.html'


	def get_success_url(self):
		return reverse('home')



	def get_object(self):
		return self.request.user









