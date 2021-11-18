def lunes(variable):
	print(variable)

def martes(variable):
	print('martes')

def miercoles(variable):
	print('miércoles')

def jueves(variable):
	print('jueves')

def viernes(variable):
	print('viernes')

def sabado(variable):
	print('sábado')

def domingo(variable):
	print('domingo')

def error(variable):
	print('error')

switch_semana = {
	1: lunes,
	2: martes,
	3: miercoles,
	4: jueves,
	5: viernes,
	6: sabado,
	7: domingo
}

dia = 10

#tomamos la función asociada a la variable y la invocamos
switch_semana.get(dia, error)(dia)