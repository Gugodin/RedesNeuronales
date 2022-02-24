from cmath import sqrt
from tempfile import tempdir
import numpy as np
import random as rand

# X =[
#     [1,0,0,0,0,0],
#     [1,1,0,0,0,0],
#     [1,0,1,0,0,0],
#     [1,1,1,0,0,0],
#     [1,0,0,1,0,0],
#     [1,1,0,1,0,0],
#     [1,0,1,1,0,0],
#     [1,1,1,1,0,0],
#     [1,0,0,0,1,0],
#     [1,1,0,0,1,0],
#     [1,0,1,0,1,0],
#     [1,1,1,0,1,0],
#     [1,0,0,1,1,0],
#     [1,1,0,1,1,0],
#     [1,0,1,1,1,0],
#     [1,1,1,1,1,0],
#     [1,0,0,0,0,1],
#     [1,1,0,0,0,1],
#     [1,0,1,0,0,1],
#     [1,1,1,0,0,1],
#     [1,0,0,1,0,1],
#     [1,1,0,1,0,1],
#     [1,0,1,1,0,1],
#     [1,1,1,1,0,1],
#     [1,0,0,0,1,1],
#     [1,1,0,0,1,1],
#     [1,0,1,0,1,1],
#     [1,1,1,0,1,1],
#     [1,0,0,1,1,1],
#     [1,1,0,1,1,1],
#     [1,0,1,1,1,1],
#     [1,1,1,1,1,1],
# ]

# Y = [[0] for i in range(31)]
# Y.append([1])


# list = [round(rand.random(),3) for i in range(3)]
n = 0.4

X = np.array([
    [1,0,0],
    [1,1,0],
    [1,0,1],
    [1,1,1]
]).transpose()

Y= np.array([0,0,0,1])

k = 0
wk = np.array([(0.854,0.327,0.558)])

print('---------------------------')
print('DATOS INICIALES')
print(f'Generacion = {k}')
print(f'W = {wk}')
print(f'N = {n}')
print('---------------------------')

while(True):
    k += 1
    uk = np.dot(wk,X)

    yck = np.array([0 if uk[0][i] < 0 else 1  for i in range(len(uk[0]))])

    ek = Y-yck

    temp = np.dot(X,ek) * n

    wt = wk + temp

    cont = 0

    for i in range(len(ek)):
        cont += ek[i]**2

    print('---------------------------')
    print('DATOS')
    print(f'Generacion = {k}')
    print(f'W = {wk}')
    print(f'Uk = {uk}')
    print(f'Yck = {yck}')
    print(f'Ek = {ek}')
    print(f'wt = {wt}')
    print(f'error = Raiz de {cont}')
    print('---------------------------')

    wk = wt
    if np.all(yck == Y):
        print(f'Y calculada = {yck}')
        print(f'Y deseada = {Y}')
        break

    

    
