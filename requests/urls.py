from django.urls import path

from .views import home, accept_view, delete_view, RequestDetailView

urlpatterns = [
    path('', home, name='home'),
    path('accept/<int:pk>/', accept_view, name='accept'),
    path('delete/<int:pk>/', delete_view, name='delete'),
    path('detail/<int:pk>/', RequestDetailView.as_view(), name='detail'),

]

