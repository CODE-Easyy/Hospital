from django import forms
from .models import Patient


GENDER_CHOICES = [
	('...', '. . .'),
	('Male', 'Male'),
	('Female', 'Female'),
]

STATUS = [
	('...', '. . .'),
	("ALKAW", "ALKAW"),
	("KRAS", "KRAS"),
]
EDUCATION = [
	("ALKAW", "ALKAW"),
	("KRAS", "KRAS"),
]

SUICIDE = [
	("ALKAW", "ALKAW"),
	("KRAS", "KRAS"),
]

YEARS= [x for x in range(1930,2020)]

class PatientForm(forms.ModelForm):
		firstname = forms.CharField(label='Имя',
					widget=forms.TextInput(
						attrs={'class': 'form-control',
						'placeholder': 'Имя'}))
		lastname = forms.CharField(label='Имя',
					widget=forms.TextInput(
						attrs={'class': 'form-control',
						'placeholder': 'Фамилия'}))
		middlename = forms.CharField(label='Имя',
					widget=forms.TextInput(
						attrs={'class': 'form-control',
						'placeholder': 'Очество'}))
		birth_date= forms.DateField(
					widget=forms.SelectDateWidget(years=YEARS,attrs = {
						'class': 'form-control',
						'placeholder': 'Дата рождения'
						}))
		gender= forms.CharField(
					widget=forms.Select(choices=GENDER_CHOICES))
		status = forms.CharField(
					widget=forms.Select(choices=STATUS, attrs = {
						'class':'form-control'
						}))
		education = forms.CharField(
					widget=forms.Select(choices=EDUCATION, attrs = {
						'class':'form-control'
						}))

		activity = forms.CharField(label='Деятельность',
					widget=forms.TextInput(
						attrs={'class': 'form-control',
						'placeholder': 'Деятельность '}))
		phone = forms.IntegerField(label='Номер карты пациента',
					widget=forms.NumberInput(
						attrs={'class': 'form-control',
						'placeholder': 'Номер карты пациента '}))
		diagnos = forms.CharField(label='Клинический диагноз',
					widget=forms.TextInput(
						attrs={'class': 'form-control',
						'placeholder': 'Клинический диагноз '}))
		data_diagnos = forms.DateField(
					widget=forms.SelectDateWidget(years=YEARS, attrs = {
						'class': 'form-control'
						}))
		suicide = forms.CharField(
					widget=forms.Select(choices=SUICIDE, attrs = {
						'class': 'form-control'
						}))


		class Meta(object):
			model = Patient
			fields = ('firstname', 'lastname', 'middlename', 'birth_date', 'gender', 'status', 'education',
				'activity', 'phone', 'diagnos', 'data_diagnos', 'suicide')