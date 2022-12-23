t = '12'

val = '2022-12-01'

val = str(val).split()
date = val[0].split('-')
date_ = date[3::-1]

val = f'{"/".join(date_)}'

print(val[3:5])

if t == val[3:5]:
    print('pegou')