# from cmath import sqrt
from asyncore import read
from cProfile import label
import math
from tempfile import tempdir
# from tkinter import E
import numpy as np
import random as rand
import sys
import matplotlib.lines as mlines

import matplotlib.pyplot as plt

from view.MainView import Ui_MainWindow
from PySide6.QtWidgets import *

import pandas as pd

    


X =[]

Y = []


def readData():
    global X
    global Y
    data = pd.read_csv('./data/dataset.csv')
    
    # print(len(data))

    for i in range(len(data)):
        X.append([1,data['X1'][i]])
        Y.append(data['Y'][i])

    # print(X)
   
# Y.append(1)
readData()



X = np.array(X).transpose()

# print(X)

Y = np.array(Y)


def entrenamiento (n,wk): 
    # print('INICIOOOOOOOOOOOOOOOOOOOOOOOOOOOoo')
    # print(n)
    # print(wk)
    k = 0

    errores = []
    generaciones = []

    while(True):
        k += 1

        uk = np.dot(wk,X)

        yck = uk

        ek = Y - yck
        
        # print(Y) 
        # print(yck) 
        # print(f'Ek: {ek}')


        mError = max(ek)
        # print(f'errores {ek}')
        # print(f'Maximo error {mError}')
        # print('X')
        # print(X.shape)
        # print('EK')
        ek = ek.transpose()
        # print(ek.transpose().shape)
        temp = np.dot(X,ek) * n

        wt = wk + temp

        cont = 0
        # print(f'Ek: {ek}')
        # print(f'len : {len(ek)}')

        for i in range(len(ek)):
            cont += ek[i]**2

        wk = wt
        print(mError)
        # print(f'cont {cont}')
        # print(f'Error a meter {math.sqrt(cont)}')
        errores.append((math.sqrt(cont)))
        generaciones.append(k)

        if  mError < 0.1:
            # print(f'pesos: {wk}')
            print(f'yck {yck}')
            # for i in yck:
            print(wk)
            print('GENERACIONES')
            print(k)
            return errores,generaciones,wk
            # return False
        # if k == 2:
        #     break 

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
            for i in range(2):
                self.wk.append(rand.uniform(0,1))
            
        else:
            t = self.ui.ws.text().strip().split(',')

            for i in range(len(t)):
                self.wk.append(float(t[i]))

        self.ns.append(float(self.ui.n1.text()))
        # self.ns.append(float(self.ui.n2.text()))
        # self.ns.append(float(self.ui.n3.text()))
        # self.ns.append(float(self.ui.n4.text()))
        # self.ns.append(float(self.ui.n5.text()))
        
        for i in range(1):
            self.curvas.append(entrenamiento(self.ns[i], self.wk))
            # print([2])


        # print(self.curvas[2])
        # print("te amo we, tqm mucho asi que pasame la tarea xfa con cariño el ovilla lame huevos")

        figure2 = plt.figure(figsize=(15, 7))

        ax = plt.subplot(1,2,1)

        
        ax.set_title('Grafica')

        for x in range(len(self.curvas)):
            ax.plot(self.curvas[x][1], self.curvas[x][0],label=f'N={self.ns[x]}')

        ax.legend()

        ax2 = plt.subplot(1,2,2)
        ax2.axis('tight')
        ax2.axis('off')

        table = [['η','Ultimos pesos de W']]
        
        for y in range(len(self.ns)):   

            
            redo = []

            for f in range(len(self.curvas[y][2])):
                redo.append(round(self.curvas[y][2][f],3))

            table.append([self.ns[y],redo])

        table = ax2.table(cellText = table, loc = 'center', cellLoc = 'center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1,3)

        plt.tight_layout()
        plt.show()

        
            
    def generateMapRand(self):
        
        for x in range(2):
            self.wk.append(rand.uniform(0,1))

        for n in range(5):
            self.ns.append(round(rand.uniform(1,0), 3))
        
        for i in range(len(self.ns)):
            self.curvas.append(entrenamiento(self.ns[i], self.wk))


        figure2 = plt.figure(figsize=(15, 7))

        ax = plt.subplot(1,2,1)

        
        ax.set_title('Grafica')

        for x in range(len(self.curvas)):
            ax.plot(self.curvas[x][1], self.curvas[x][0], marker='o',label=f'N={self.ns[x]}')

        ax.legend()

        ax2 = plt.subplot(1,2,2)
        ax2.axis('tight')
        ax2.axis('off')

        table = [['η','Ultimos pesos de W']]
        
        for y in range(len(self.ns)):   
            redo = []
            for f in range(len(self.curvas[y][2])):
                redo.append(round(self.curvas[y][2][f],3))

            table.append([self.ns[y],redo])

        table = ax2.table(cellText = table, loc = 'center', cellLoc = 'center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1,3)

        plt.tight_layout()
        plt.show()




if __name__ == '__main__':


    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec())

    # entrenamiento(0.0000001,[np.random.uniform(0,1),np.random.uniform(0,1)])
    
    # print('')
    
