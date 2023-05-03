from functools import reduce
def impares(item):  
  if item % 2 > 0:
    return True
  return False
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n = filter(impares,lista)
resultList = list(n)
sumatoria = reduce(lambda a,b:a+b,resultList)
print(resultList)
print(sumatoria)
