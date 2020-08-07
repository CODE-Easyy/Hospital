"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from accounts.views import RegistrationView, login_page, ProfileView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home'),

    path('hospital/', include(('hospitals.urls', 'hospital'))),
    path('patient/', include(('patients.urls', 'patient'))),
    path('register/', RegistrationView.as_view(), name = 'register'),
    path('login/', login_page, name = 'login'),

    path('profile-update', ProfileView.as_view(), name='profile-update'),

    


    path('admin_panel/hospitals/', include(('hospitals.urls', 'hospital'))),
    path('admin_panel/requests/', include(('requests.urls', 'request'))),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
