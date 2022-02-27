# from cmath import sqrt
from cProfile import label
import math
from tempfile import tempdir
import numpy as np
import random as rand
import sys
import matplotlib.lines as mlines

import matplotlib.pyplot as plt

from view.MainView import Ui_MainWindow
from PySide6.QtWidgets import *

X =[
    [1,0,0,0,0,0],
    [1,1,0,0,0,0],
    [1,0,1,0,0,0],
    [1,1,1,0,0,0],
    [1,0,0,1,0,0],
    [1,1,0,1,0,0],
    [1,0,1,1,0,0],
    [1,1,1,1,0,0],
    [1,0,0,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,0,1,0],
    [1,1,1,0,1,0],
    [1,0,0,1,1,0],
    [1,1,0,1,1,0],
    [1,0,1,1,1,0],
    [1,1,1,1,1,0],
    [1,0,0,0,0,1],
    [1,1,0,0,0,1],
    [1,0,1,0,0,1],
    [1,1,1,0,0,1],
    [1,0,0,1,0,1],
    [1,1,0,1,0,1],
    [1,0,1,1,0,1],
    [1,1,1,1,0,1],
    [1,0,0,0,1,1],
    [1,1,0,0,1,1],
    [1,0,1,0,1,1],
    [1,1,1,0,1,1],
    [1,0,0,1,1,1],
    [1,1,0,1,1,1],
    [1,0,1,1,1,1],
    [1,1,1,1,1,1],
]

Y = [0 for i in range(31)]
Y.append(1)



X = np.array(X).transpose()

Y = np.array(Y)


def neurona (n,wk): 
    k = 0

    # print('---------------------------')
    # print('DATOS INICIALES')
    # print(f'Generacion = {k}')
    # print(f'W = {wk}')
    # print(f'N = {n}')
    # print('---------------------------')

    errores = []
    generaciones = []

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

        # print('---------------------------')
        # print('DATOS')
        # print(f'Generacion = {k}')
        # print(f'W = {wk}')
        # print(f'Uk = {uk}')
        # print(f'Yck = {yck}')
        # print(f'Ek = {ek}')
        # print(f'wt = {wt}')
        # print(f'error = Raiz de {cont}')
        # print('---------------------------')

        wk = wt
        errores.append((math.sqrt(cont)))
        generaciones.append(k)

        if np.all(yck == Y):
            # print(f'Y calculada = {yck}')
            # print(f'Y deseada = {Y}')
            
            return errores,generaciones,list(wk[0])

class Ventana(QMainWindow):
    wk = []
    ns = []

    curvas = []

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.generarGrafica.clicked.connect(self.generateMap)
        self.ui.allRandom.clicked.connect(self.generateMapRand)

    def generateMap(self):

        if self.ui.ws.text() == '':
            for i in range(6):
                self.wk.append(round(rand.random(),3))
            
        else:
            t = self.ui.ws.text().strip().split(',')

            for i in range(len(t)):
                self.wk.append(float(t[i]))

        self.ns.append(float(self.ui.n1.text()))
        self.ns.append(float(self.ui.n2.text()))
        self.ns.append(float(self.ui.n3.text()))
        self.ns.append(float(self.ui.n4.text()))
        self.ns.append(float(self.ui.n5.text()))
        
        for i in range(len(self.ns)):
            self.curvas.append(neurona(self.ns[i], np.array([tuple(self.wk)])))


        figure2 = plt.figure(figsize=(15, 10))

        ax = plt.subplot(1,1,1)

        print(self.ns[0])
        print(self.curvas[0])

        ax.set_title('Grafica')
        for x in range(len(self.curvas)):
            ax.plot(self.curvas[x][1], self.curvas[x][0], marker='o',label=f'N={self.ns[x]}')

        ax.legend()

        plt.show()

        
            
    def generateMapRand(self):
        
        for x in range(6):
            self.wk.append(round(rand.random(),3))
        
        for n in range(5):
           self.ns.append(round(rand.uniform(1,0), 3))

if __name__ == '__main__':

    # print(neurona(0.4,wk))

    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec())
    

    
