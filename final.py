from visual.graph import *

N=raw_input('N? ')#numero de masas
if N=='':N=2
N=int(N)

h=0.05
t=0.0
k=1.0
m=1.0

ss=zeros(2*N)#estado inicil delsistema
ss[0]=1.0
if N==2:
    ss[1]=-1.0#modo normal
if N==3:
    ss[1]=-1.0*sqrt(2)
    ss[2]=+1.0

display(title='Sistema masa resorte para N masas',width=1200,height=200)
display(title='Posiciones vs tiempo',y=220,width=1200)
#lineas antre la line a 21 y 50
#funcion grafica por definir
def graficar(ss):
    ss[0]=0
#apartir de linea 50
M=2*k/m*eye(N)+k/m*(eye(N,k=1)+eye(N,k=-1))
a=concatenate((0*eye(N),M))
b=concatenate((eye(N),0*eye(N)))
M=concatenate((a,b),axis=1)
print M

def f(ss):
    return dot(M,ss)
def rk4(ss):
    k1=h*f(ss)
    k2=h*f(ss+0.5*k1)
    k3=h*f(ss+0.5*k2)
    k4=h*f(ss+k3)
    return ss+(k1+2*k2+2*k3+k4)/6

while 1:
    rate(80)
    graficar(ss)