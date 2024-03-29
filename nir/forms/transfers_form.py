from django import forms
from django.forms import CharField, DateTimeField, DateTimeInput

from nir.models import (Transferencias_Adu, Transferencias_Ges,
                        Transferencias_Ped)


class FormAdul(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Transferencias_Adu
        fields = 'date_reg_transf','date_transf','pac','data_nasc','mtv_dgt','dest','munic','espec','scd','acomp','ambul','local_ambul','contref','obs',
        labels = {
            'date_reg_transf':'Data REG Transferência: ',
            'date_transf':'Data Transferência: ',
            'pac':'Paciente: ',
            'data_nasc':'Data de Nascimento: ',
            'mtv_dgt':'Motivo/Diagnostico: ',
            'dest':'Destino: ',
            'munic':'Município: ',
            'espec':'Especialidade: ',
            'scd':'Senha Central de Leitos: ',
            'acomp':'Acompanhamento: ',
            'ambul':'Ambulância: ',
            'local_ambul':'Local Ambulância: ',
            'contref':'Contrareferencia: ',
            'obs':'Obs: ',
        }
        widgets = {
            'date_reg_transf': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Ex: 01/01/2022 00:00:00',
                }
            ),
            'date_transf': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Ex: 01/01/2022 00:00:00',
                }
            ),
            'data_nasc': forms.DateInput(
                attrs={
                    'placeholder': 'Ex: 01/01/2022',
                }
            )
        }


class FormGes(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Transferencias_Ges
        fields = 'date_reg_transf','date_transf','pac','data_nasc','mtv_dgt','dest','munic','espec','scd','acomp','ambul','local_ambul','contref','obs',
        labels = {
            'date_reg_transf':'Data REG Transferência: ',
            'date_transf':'Data Transferência: ',
            'pac':'Paciente: ',
            'data_nasc':'Data de Nascimento: ',
            'mtv_dgt':'Motivo/Diagnostico: ',
            'dest':'Destino: ',
            'munic':'Município: ',
            'espec':'Especialidade: ',
            'scd':'Senha Central de Leitos: ',
            'acomp':'Acompanhamento: ',
            'ambul':'Ambulância: ',
            'local_ambul':'Local Ambulância: ',
            'contref':'Contrareferencia: ',
            'obs':'Obs: ',
        }

        widgets = {
            'date_reg_transf': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Ex: 01/01/2022 00:00:00',
                }
            ),
            'date_transf': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Ex: 01/01/2022 00:00:00',
                }
            ),
            'data_nasc': forms.DateInput(
                attrs={
                    'placeholder': 'Ex: 01/01/2022',
                }
            )
        }
    
class FormPed(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Transferencias_Ped
        fields = 'date_reg_transf','date_transf','pac','data_nasc','mtv_dgt','dest','munic','espec','scd','acomp','ambul','local_ambul','contref','obs',
        labels = {
            'date_reg_transf':'Data REG Transferência: ',
            'date_transf':'Data Transferência: ',
            'pac':'Paciente: ',
            'data_nasc':'Data de Nascimento: ',
            'mtv_dgt':'Motivo/Diagnostico: ',
            'dest':'Destino: ',
            'munic':'Município: ',
            'espec':'Especialidade: ',
            'scd':'Senha Central de Leitos: ',
            'acomp':'Acompanhamento: ',
            'ambul':'Ambulância: ',
            'local_ambul':'Local Ambulância: ',
            'contref':'Contrareferencia: ',
            'obs':'Obs: ',
        }

        widgets = {
            'date_reg_transf': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Ex: 01/01/2022 00:00:00',
                }
            ),
            'date_transf': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Ex: 01/01/2022 00:00:00',
                }
            ),
            'data_nasc': forms.DateInput(
                attrs={
                    'placeholder': 'Ex: 01/01/2022',
                }
            )
        }