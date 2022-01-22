# -*- coding: utf-8 -*-
"""
Created on Jan 19 2020
@author: NicoMosty
"""
from os import remove
import numpy as np
import matplotlib.pyplot as plt

#___CONSTANTES__#
dr=5e-4
Beta=np.array([0.1,1,5])
Phi=np.array([5,20,50])

#_____GENERAR VECTOR DE RADIOS____#
R=np.arange(0, 1+0.1*dr, dr)
St=np.zeros(R.size)
dSt=0

def SvsR(phi,beta):
    #___DEFINICION DE SEGUNDA DERIVADA___#
    def D2S(dS,S,r):
        
        return ((phi*phi)*(beta*S/(beta+S))-2*dS/r)

    # DEFINICION VECTORES
    S=np.zeros(R.size)
    dS=np.zeros(R.size)
    d2S=np.zeros(R.size)

    # CONDICION INICIAL Y FINAL
    Sf=1
    dSo=0.005
    # PRUEBA INICIAL
    if beta>0.1:
        C1=0.3
    else:
        C1=0.6

    while True:
        for i in range(R.size):
            # Condiciones inicio
            if i==0:
                S[i]=dSo
                dS[0]=0
                d2S[0]=((phi**2)/3)*((beta*S[i])/(beta+S[i]))
                
            if i>0:
                S[i]=S[i-1]+dr*dS[i-1]
                dS[i]=dS[i-1]+dr*d2S[i-1]
                d2S[i]=D2S(dS[i],S[i],R[i])
        if S[R.size-1]<C1:
            break
        else:       
            dSo=dSo*0.1

    So=0
    C2=0
    while True:
        if 0.9<S[R.size-1] and C2==0 and beta>1:
            dSo=dSo*0.05
            C2=1
        for i in range(R.size):
            # Condiciones inicio
            if i==0:
                S[i]=So
                dS[0]=0
                d2S[0]=((phi**2)/3)*((beta*S[i])/(beta+S[i]))
                
            if i>0:
                S[i]=S[i-1]+dr*dS[i-1]
                dS[i]=dS[i-1]+dr*d2S[i-1]
                d2S[i]=D2S(dS[i],S[i],R[i])
        print("Beta={:5}|Phi={:5}|dSo={:7}|So={:9}|S[R]={:4}".format(beta,phi,dSo,So,S[R.size-1]))    
        if S[R.size-1]>0.99:
            break
        else:         
            So=So+dSo
    
    global St
    global dSt
    St=S
    dSt=dS[R.size-1]

# Matriz Concentraciones
SS=np.zeros((Phi.size,R.size))

# Matriz de Eficiencias
Ef=np.zeros((Phi.size,R.size))

# Loop de Calculo de Concentraciones Cambiando Beta y Phi
for B in Beta:
    for P in Phi:
        SvsR(P,B) 
        SS[list(Phi).index(P)]=St
        Ef[list(Beta).index(B),list(Phi).index(P)]=3*dSt/(P*P*B/(B+1))
        
        print("Beta={:5}|Phi={:5}|Ef={:5}".format(B,P,Ef[list(Beta).index(B),list(Phi).index(P)]))
        print("OK")
        print("__________________________________________")