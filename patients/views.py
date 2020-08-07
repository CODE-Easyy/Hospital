from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Patient
from .forms import PatientForm



from django.http import HttpResponse
from tablib import Dataset
from .resources import PatientResource






def home(request):
	if request.method == 'POST':
		file_format = request.POST['file-format']
		patient_resource = PatientResource()
		dataset = patient_resource.export()
		if file_format == 'CSV':
			response = HttpResponse(dataset.csv, content_type = 'text/csv')
			response['Content-Disposition'] = 'attachment; filename = "export_data.csv"'
			return response
		elif file_format == 'JSON':
			response = HttpResponse(dataset.json, content_type = 'application/json')
			response['Content-Disposition'] = 'attachment; filename = "export_data.json"'
			return response
		elif file_format == 'XLS (Excel)':
			response = HttpResponse(dataset.xls, content_type = 'application/vnd.ms-excel')
			response['Content-Disposition'] = 'attachment; filename = "export_data.xls"'
			return response

	patients = Patient.objects.all()
	paginator = Paginator(patients , 2)
	page = request.GET.get('page')
	patients = paginator.get_page(page)

	return render(request, 'patients/home.html', {'patients':patients})

class PatientCreateView(SuccessMessageMixin, CreateView):
	model = Patient
	form_class = PatientForm
	template_name = 'patients/create.html'
	success_url = reverse_lazy('patient:home')
	success_message = 'Доктор успешно создан!'

class PatientDeleteView(SuccessMessageMixin, DeleteView):
	model = Patient
	success_url = reverse_lazy('patient:home')
	def get(self, request, *args, **kwargs):
		messages.success(request, "Город успешно удален!")
		return self.post(request, *args, **kwargs)



def export_data(request):
	

	return render(request, 'patients/export.html')





