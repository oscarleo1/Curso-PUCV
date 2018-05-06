# 1. Simular datos
import argparse
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def getParser():
    parser = argparse.ArgumentParser(description='Descripcion de la funcion de este programa.')
    parser.add_argument('-o',type=str,dest="formato",help="'png' si la imagen es guardada en formato PNG,                                                            ,o 'pdf' para ser guradada en formato PDF")

    if len(sys.argv) == 1:
        print >> sys.stderr,parser.print_help()
        exit(0)
    return parser

def main():
    args=getParser().parse_args()
    formato=args.formato
    if formato=="png":
        plt.savefig("ajuste.png")
    elif formato=="pdf":
        plt.savefig("ajuste.pdf")

# Generar datos {t,y}, en donde y=sin(x)*a
t = np.linspace(0,20,200)
m,b=[2,0.5]
yy = m*t+b 
noise = np.random.normal(0,10,200)
y = yy + noise

# 2. Ajustar a datos
from scipy.optimize import leastsq
def residual(params,t,y):
    m,b=params
    model = m*t+b
    return y-model

params=[1,0]
out=leastsq(residual,params,args=(t,y))
print out
m_hat,b_hat=out[0]
fit=m_hat*t+b_hat
plt.plot(t,y,'ro')
plt.plot(t,fit)
plt.show()
plt.savefig("ajuste.png") # Codigo autoexplicativo



