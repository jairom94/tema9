paises = set()
lista_=input('Ingrese paises seprados por una (,) : ')
#'ecudor,peru,usa,tailandia,isalndia,tegucigalpa,guatemala,chile,argentina,canada,mexico,holanda'
longitud = len(lista_.split(','))
for i in range(longitud):
  paises.add(lista_.split(',')[i].strip().title())
listaOrdenada = sorted(paises)
result = ''
for i in range(longitud):  
  if i == (longitud -1):
    result += listaOrdenada[i]
  else:
    result += listaOrdenada[i] + ', '
    
print(result)
