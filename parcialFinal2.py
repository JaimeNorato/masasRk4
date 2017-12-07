from visual.graph import *
from random import randint

#numero de masas
N=3
#variables
h=0.05
t=0.0
k=1.0
m=1.0
p=6
#indica si aun hay movimiento por la ultima interaccion con la particula
movimientos=0
#estado inicil delsistema
ss=zeros(2*N)
print ss
ss[0]=-p/2
ss[1]=0.1
ss[2]=+p/2
print ss
display(title='Sistema masa resorte para N masas',y=10,width=1200,height=200)
display(title='Posiciones vs Valocidad',y=250,width=1200)

piso = box(pos=(ss[1],-1,0),length=p*N,height=0.1,width=2,material=materials.wood)


masas=[]
resortes=[]
graficas=[]
for i in range(0,N):
    col = color.magenta
    if i==1: col=color.red
    if i==2: col=color.orange
    masas.append(sphere(pos=(ss[i],0,0),color=col))
    graficas.append(gcurve(color=col))
    if i<N-1:
        resortes.append(helix(pos=(ss[i]+masas[i].radius,0,0),length=float(ss[i+1])-masas[i].radius+1,color=color.green,radius=0.3,thickness=0.3/5,coils=10.0))


#funcion grafica por definir
def graficar(ss):
    for i in range(0,N):
        print N, i, ss[0],ss[1],ss[2]
        graficas[i].plot(pos=(ss[i],ss[N+i]))
#animacion de la s masas y los resortes
def animar(ss):
    for i in range(0, N):
        masas[i].x = ss[i]
        if i < N - 1:
            resortes[i].x=ss[i]+masas[i].radius
            resortes[i].length=float(ss[i+1])-masas[i].radius+1
#construccion de la matriz
M=-2*k/m*eye(N)+k/m*(eye(N,k=1)+eye(N,k=-1))
a=concatenate((0*eye(N),M))
b=concatenate((eye(N),0*eye(N)))
M=concatenate((a,b),axis=1)
print 'ss'
print ss
print 'M'
print M
#definicion de la funcion f
def f(ss):
    return dot(M,ss)
#definicion de la funcion rk4
def rk4(ss):
    k1=h*f(ss)
    k2=h*f(ss+k1/2)
    k3=h*f(ss+k2/2)
    k4=h*f(ss+k3)
    return ss+(k1+2*k2+2*k3+k4)/6
#funcion que determina si la particula interactua con el resorte
def interactua():
    global movimientos
    mueve=False
    num=randint(0,15)
    if(num==9):
        mueve=True
        movimientos+=1
    return mueve
#determina si aun se esta moviendo las masas a causa de la ineraccion con la particula
def seMueve(ss):
    global movimientos
    mueve=false
    if((ss[1]-ss[0])<=0 or (ss[2]-ss[1])<=0):
        movimientos-=1
    if(movimientos>=0): mueve=True
    return mueve
#ciclo wile que actualiza la grafica, la animacion y variables
while 1:
    rate(80)
    graficar(ss)
    animar(ss)
    if(interactua() or seMueve(ss)):
        ss = rk4(ss)
