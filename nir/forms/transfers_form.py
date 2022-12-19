from django import forms

from nir.models import (Transferencias_Adu, Transferencias_Ges,
                        Transferencias_Ped)


class FormAdul(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Transferencias_Adu
        fields = 'date_reg_transf', #0 - DATETIME
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

class FormGes(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Transferencias_Ges
        fields = 'date_reg_transf', #0 - DATETIME
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
    
class FormPed(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Transferencias_Ped
        fields = 'date_reg_transf', #0 - DATETIME
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