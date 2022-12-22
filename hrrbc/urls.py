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
    path('dashboard/transf/new', views.dashboard_transf_new, name='transf_new'),
    path('dashboard/transf/<int:id>', views.dashboard_transf_view, name='dashboard_view'),
    path('dashboard/transf/<int:id>/edit/', views.dashboard_transf_edit, name='transf_edit'),
    path('dashboard_ped/', views.dashboard_ped, name='dashboard_ped'),
    path('dashboard_ped/transf/<int:id>/edit/', views.ped_transf_edit, name='transf_ped_edit'),
    path('dashboard_ped/transf/new', views.ped_transf_new, name='transf_ped_new'),
    path('dashboard_ped/transf/<int:id>', views.ped_transf_view, name='transf_ped_view'),
    path('dashboard_ges/', views.dashboard_ges, name='dashboard_ges'),
    path('dashboard_ges/transf/<int:id>/edit/', views.ges_transf_edit, name='transf_ges_edit'),
    path('dashboard_ges/transf/new', views.ges_transf_new, name='transf_ges_new'),
    path('dashboard_ges/transf/<int:id>', views.ges_transf_view, name='transf_ges_view'),
    path('dashboard/trasnf/<int:id>/delete', views.dashboard_transf_delete, name='trasnf_delete'),
    path('dashboard/trasnf_ped/<int:id>/delete', views.dashboard_transf_ped_delete, name='trasnf_ped_delete'),
    path('dashboard/trasnf_ges/<int:id>/delete', views.dashboard_transf_ges_delete, name='trasnf_ges_delete'),
    path('export/xlsx', views.exportar_xls, name='export_xls'),
]
