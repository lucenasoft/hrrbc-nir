from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from nir import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/')),
    path('login/', views.login_view, name='login'),
    path('create/', views.login_create, name='login_create'),
]
