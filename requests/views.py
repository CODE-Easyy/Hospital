from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView



from accounts.models import Doctor


def home(request):
  if request.GET.get(id):
    print(request.GET.get(id))
  not_accepted_doctors = Doctor.objects.filter(is_accept=False, is_staff=False)
  # not_accepted_doctors = Doctor.objects.all()
  context = {'objects': not_accepted_doctors}
  return render(request, 'requests/home.html', context)

def accept_view(request, pk=None):
  if pk:
    object = Doctor.objects.get(pk=pk)
    object.is_accept = True
    object.save()
  return redirect('request:home')

def delete_view(request, pk=None):
  if pk:
    object = Doctor.objects.get(pk=pk)
    object.delete()
  return redirect('request:home')


class RequestDetailView(DetailView):
	queryset = Doctor.objects.all()
	context_object_name = 'object'
	template_name = 'requests/detail.html'