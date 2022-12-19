from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from django.urls import reverse

from nir.models import (Transferencias_Adu, Transferencias_Ges,
                        Transferencias_Ped)

from .forms import LoginForm


def login_view(request):
    form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
        'form_action': reverse('login_create')
    })

def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect(reverse('dashboard'))

        else:
            messages.error(request, 'Login ou senha incorretos.')

    return redirect(login_url)

@login_required(login_url='login', redirect_field_name='next')
def dashboard(request):
    transfer = Transferencias_Adu.objects.filter(
    author=request.user
    ).order_by('-id')
    #search = request.GET.get('search')
    #if search:
        #called = called.filter(user_requester__icontains=f'{search}')
    return render(request, 'dashboard.html', context={
        'transfers': transfer,
    })

@login_required(login_url='login', redirect_field_name='next')
def dashboard_ped(request):
    transfer = Transferencias_Ped.objects.filter(
    author=request.user
    ).order_by('-id')
    #search = request.GET.get('search')
    #if search:
        #called = called.filter(user_requester__icontains=f'{search}')
    return render(request, 'dashboard_ped.html', context={
        'transfers': transfer,
    })

@login_required(login_url='login', redirect_field_name='next')
def dashboard_ges(request):
    transfer = Transferencias_Ges.objects.filter(
    author=request.user
    ).order_by('-id')
    #search = request.GET.get('search')
    #if search:
        #called = called.filter(user_requester__icontains=f'{search}')
    return render(request, 'dashboard_ges.html', context={
        'transfers': transfer,
    })

@login_required(login_url='login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('login'))

    logout(request)
    return redirect(reverse('login'))
