from django.db import models

class Patient(models.Model):
	firstname = models.CharField(max_length = 50, verbose_name = 'Имя')
	lastname = models.CharField(max_length = 50, verbose_name = 'Фамилия')
	middlename = models.CharField(max_length = 50, verbose_name = 'Очество' )
	birth_date= models.DateField(verbose_name= 'Дата рождения')
	gender= models.CharField(max_length=6, verbose_name = 'Пол' )
	status = models.CharField(max_length = 15, verbose_name = 'Семейный статус')
	education = models.CharField(max_length = 100, verbose_name = 'Образование')
	activity = models.CharField(max_length = 100, verbose_name = 'Деятельность')
	phone = models.CharField(max_length = 20, verbose_name = 'Номер карты пациента')
	diagnos = models.CharField(max_length = 100, verbose_name = 'Клинический диагноз')
	data_diagnos = models.DateField(verbose_name = 'Дата установления диагноза')
	suicide = models.CharField(max_length = 10, verbose_name = 'Суицидальный риск')

	def __str__(self):
		return "{} {} {}".format(self.firstname, self.lastname, self.middlename)


	class Meta:
		verbose_name = 'Пациент'
		verbose_name_plural = 'Пациенты'
		ordering = ['id']
