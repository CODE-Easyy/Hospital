from django.shortcuts import render


from .models import Hospital



def home(request):
  hospitals = Hospital.objects.all()
  context = {'objects': hospitals}
  return render(request, 'hospitals/home.html', context)
