from datetime import date, datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from nir.actions.export_xlsx import export_xlsx
from nir.forms.transfers_form import FormAdul, FormGes, FormPed
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
    transfer = Transferencias_Adu.objects.all().order_by('-id')
    pac_search = request.GET.get('pac')
    date_search = request.GET.get('date')
    scd = request.GET.get('scd')
    if pac_search:
        transfer = transfer.filter(pac__icontains=f'{pac_search}')
    if date_search:
        transfer = transfer.filter(date_transf__icontains=f'{date_search}')
    if scd:
        transfer = transfer.filter(scd__icontains=f'{scd}')
    return render(request, 'dashboard.html', context={
        'transfers': transfer,
    })

@login_required(login_url='login', redirect_field_name='next')
def dashboard_ped(request):
    transfer = Transferencias_Ped.objects.all().order_by('-id')
    pac_search = request.GET.get('pac')
    date_search = request.GET.get('date')
    scd = request.GET.get('scd')
    if pac_search:
        transfer = transfer.filter(pac__icontains=f'{pac_search}')
    if date_search:
        transfer = transfer.filter(date_transf__icontains=f'{date_search}')
    if scd:
        transfer = transfer.filter(scd__icontains=f'{scd}')
    return render(request, 'dashboard_ped.html', context={
        'transfers': transfer,
    })

@login_required(login_url='login', redirect_field_name='next')
def dashboard_ges(request):
    transfer = Transferencias_Ges.objects.all().order_by('-id')
    pac_search = request.GET.get('pac')
    date_search = request.GET.get('date')
    scd = request.GET.get('scd')
    if pac_search:
        transfer = transfer.filter(pac__icontains=f'{pac_search}')
    if date_search:
        transfer = transfer.filter(date_transf__icontains=f'{date_search}')
    if scd:
        transfer = transfer.filter(scd__icontains=f'{scd}')
    return render(request, 'dashboard_ges.html', context={
        'transfers': transfer,
    })

@login_required(login_url='login', redirect_field_name='next')
def dashboard_transf_view(request, id):
    transf = get_object_or_404(Transferencias_Adu, pk=id)
    return render(request, 'transf_view.html', context={
        'transf': transf,
        'return_adu': True
    })

@login_required(login_url='login', redirect_field_name='next')
def ped_transf_view(request, id):
    transf = get_object_or_404(Transferencias_Ped, pk=id)
    return render(request, 'transf_view.html', context={
        'transf': transf,
        'return_ped': True
    })

@login_required(login_url='login', redirect_field_name='next')
def ges_transf_view(request, id):
    transf = get_object_or_404(Transferencias_Ges, pk=id)
    return render(request, 'transf_view.html', context={
        'transf': transf,
        'return_ges': True
    })

@login_required(login_url='login', redirect_field_name='next')
def dashboard_transf_new(request):
    form = FormAdul(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        transf: Transferencias_Adu = form.save(commit=False)

        transf.author = request.user
        transf.author_reg = datetime.now()

        transf.save()

        messages.success(request,'Transferência registrada!')
        return redirect(reverse('dashboard')) #LEMBRAR DE REDIRECIONAR PARA O CANTO DE CADA UM
    
    return render(request, 'new_transf.html', context= {
        'form': form, #CRIAR O TEMPLATE DAQUI
        'return_adu': True
    })

@login_required(login_url='login', redirect_field_name='next')
def ped_transf_new(request):
    form = FormPed(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        transf: Transferencias_Ped = form.save(commit=False)

        transf.author = request.user
        transf.author_reg = datetime.now()

        transf.save()

        messages.success(request,'Transferência registrada!')
        return redirect(reverse('dashboard_ped')) #LEMBRAR DE REDIRECIONAR PARA O CANTO DE CADA UM
    
    return render(request, 'new_transf.html', context= {
        'form': form, #CRIAR O TEMPLATE DAQUI
        'return_ped': True
    })

@login_required(login_url='login', redirect_field_name='next')
def ges_transf_new(request):
    form = FormGes(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        transf: Transferencias_Ges = form.save(commit=False)

        transf.author = request.user
        transf.author_reg = datetime.now()

        transf.save()

        messages.success(request,'Transferência registrada!')
        return redirect(reverse('dashboard_ges')) #LEMBRAR DE REDIRECIONAR PARA O CANTO DE CADA UM
    
    return render(request, 'new_transf.html', context= {
        'form': form, #CRIAR O TEMPLATE DAQUI
        'return_ges': True
    })

@login_required(login_url='login', redirect_field_name='next')
def dashboard_transf_edit(request, id):
    transf = Transferencias_Adu.objects.get(
        pk=id,
    )

    if not transf:
        raise Http404()

    form = FormAdul(
        data=request.POST or None,
        files=request.FILES or None,
        instance=transf
    )

    if form.is_valid():
        transf = form.save(commit=False)
        form.save()
        messages.success(request,'Transferência alterada com sucesso!')
        return redirect(reverse('dashboard'))

    return render(request,'edit_transf.html', context={
        'transf': transf,
        'form': form,
        'return_adu': True
    })

@login_required(login_url='login', redirect_field_name='next')
def ges_transf_edit(request, id):
    transf = Transferencias_Ges.objects.get(
        pk=id,
    )

    if not transf:
        raise Http404()

    form = FormGes(
        data=request.POST or None,
        files=request.FILES or None,
        instance=transf
    )

    if form.is_valid():
        transf = form.save(commit=False)
        form.save()
        messages.success(request,'Transferência alterada com sucesso!')
        return redirect(reverse('dashboard_ges'))

    return render(request,'edit_transf.html', context={
        'transf': transf,
        'form': form,
        'return_ges': True
    })

@login_required(login_url='login', redirect_field_name='next')
def ped_transf_edit(request, id):
    transf = Transferencias_Ped.objects.get(
        pk=id,  
    )

    if not transf:
        raise Http404()

    form = FormPed(
        data=request.POST or None,
        files=request.FILES or None,
        instance=transf
    )

    if form.is_valid():
        transf = form.save(commit=False)
        form.save()
        messages.success(request,'Transferência alterada com sucesso!')
        return redirect(reverse('dashboard_ped'))

    return render(request,'edit_transf.html', context={
        'transf': transf,
        'form': form,
        'return_ped': True
    })

@login_required(login_url='login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('login'))

    logout(request)
    return redirect(reverse('login'))

@login_required(login_url='login', redirect_field_name='next')
def exportar_xls(request):
    if request.method == 'POST':
        date_xls_post = request.POST.get('data_xls')
        day = (date_xls_post[8:10])
        year = (date_xls_post[0:4])
        date_xls_post = str(date_xls_post[5:7]).strip('0')
    MDATA = datetime.now().strftime('%d-%m-%Y')
    filename = 'TRANSFERÊNCIAS ADULTOS.xls'
    _filename = filename.split('.')
    filename_final = f'{_filename[0]} {MDATA}.{_filename[1]}'
    start = date(int(year), int(date_xls_post), 1)
    end = date(int(year), int(date_xls_post), int(day))
    queryset = Transferencias_Adu.objects.filter(date_transf__range=[start, end]).values_list(
        'date_reg_transf', #0 - DATETIME
        'date_transf', #1 - DATETIME
        'pac',
        'data_nasc', #3 - DATE
        'mtv_dgt',
        'dest',
        'munic',
        'espec',
        'scd',
        'acomp',
        'ambul',
        'local_ambul',
        'contref',
        'obs',
        'author__first_name',
        'author_reg', #15 - DATETIME
    )
    queryset2 = Transferencias_Ped.objects.filter(date_transf__range=[start, end]).values_list(
        'date_reg_transf', #0 - DATETIME
        'date_transf', #1 - DATETIME
        'pac',
        'data_nasc', #3 - DATE
        'mtv_dgt',
        'dest',
        'munic',
        'espec',
        'scd',
        'acomp',
        'ambul',
        'local_ambul',
        'contref',
        'obs',
        'author__first_name',
        'author_reg', #15 - DATETIME
    )
    queryset3 = Transferencias_Ges.objects.filter(date_transf__range=[start, end]).values_list(
        'date_reg_transf', #0 - DATETIME
        'date_transf', #1 - DATETIME
        'pac',
        'data_nasc', #3 - DATE
        'mtv_dgt',
        'dest',
        'munic',
        'espec',
        'scd',
        'acomp',
        'ambul',
        'local_ambul',
        'contref',
        'obs',
        'author__first_name',
        'author_reg', #15 - DATETIME
    )
    columns = ('DATA REG TRANSFERÊNCIA','DATA TRANSFERÊNCIA','PACIENTE','DATA NASCIMENTO','MOTIVO/DIAGNOSTICO','DESTINO','MUNICÍPIO','ESPECIALIDADE','SENHA CENTRAL DE LEITOS','ACOMPANHAMENTO','AMBULÂNCIA','LOCAL AMBULÂNCIA','CONTRAREFERENCIA','OBS','REGISTRADOR','DATA DO REGISTRO',)
    response = export_xlsx(filename_final, queryset, queryset2, queryset3, columns)
    return response

@login_required(login_url='login', redirect_field_name='next')
def dashboard_transf_delete(request,id):
    transf = Transferencias_Adu.objects.filter(
        pk=id,
    ).first()

    if not transf:
        raise Http404()

    transf.delete()
    messages.success(request, 'Transferência deletada com sucesso.')
    return redirect(reverse('dashboard'))

@login_required(login_url='login', redirect_field_name='next')
def dashboard_transf_ped_delete(request,id):
    transf = Transferencias_Ped.objects.filter(
        pk=id,
    ).first()

    if not transf:
        raise Http404()

    transf.delete()
    messages.success(request, 'Transferência deletada com sucesso.')
    return redirect(reverse('dashboard_ped'))

@login_required(login_url='login', redirect_field_name='next')
def dashboard_transf_ges_delete(request,id):
    transf = Transferencias_Ges.objects.filter(
        pk=id,
    ).first()

    if not transf:
        raise Http404()

    transf.delete()
    messages.success(request, 'Transferência deletada com sucesso.')
    return redirect(reverse('dashboard_ges'))