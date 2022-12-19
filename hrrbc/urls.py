from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from nir import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='dashboard/')),
    path('login/', views.login_view, name='login'),
    path('create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_ped/', views.dashboard_ped, name='dashboard_ped'),
    path('dashboard_ges/', views.dashboard_ges, name='dashboard_ges'),
]
