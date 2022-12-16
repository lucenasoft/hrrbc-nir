# Sistema de Registro NIR

Sistema para registro de paciêntes transferidos, com gerador de lavantamento e filtros para relatórios.




## Stack utilizada

**Front-end:** Django, JavaScript, CSS, HTML

**Back-end:** Python, Django


## Levantamento de Requesitos

- Gerar projeto e app - X
- Modular banco de dados com campos da planilha - X
- Modelagem do banco
- Modelagem e criação de pagina de login


## Atualizações obrigatórias

- Adicionar o anti-refresh nas paginas

## Campos para o baco

Tabela municipio.

campos:

NOME - CHARFILD

Tabela transferencia.

campos:

DATA E HORA DO REGISTRO DE TRANSF - DATATIMEFILD
DATA E HORA DA SAIDA - DATETIMEFILD
PACIENTE - CHARFILD
DATA NASCIMENTO - DATETIMEFILD
MOTIVO/DIAGNOSTICO - CHARFILD
DESTINO - CHARFILD
FOREING - TABELA MUNICIPIOS
ESPECIALIDADE - CHARFILD
SENHA CENTRAL DE - INTEGER
AMBULÂNCIA - CHARCHOICE FOR "BÁSICA" OR "UTI"
ACOMPANHANTE - CHARCHOICE FOR "BÁSICA" OR "UTI"
CONTRAREFERÊNCIA - CHARFIELD
OBS - TEXTFIELD