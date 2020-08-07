from django.urls import path
from .views import home, PatientCreateView, PatientDeleteView, export_data

urlpatterns = [
    path('', home, name = 'home'),
    path('export/', export_data, name = 'export'),
    path('create/', PatientCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', PatientDeleteView.as_view() , name = 'delete'),


]