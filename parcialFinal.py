from visual.graph import *
from random import randint

#numero de masas
N=3

h=0.05
t=0.0
k=1.0
m=1.0
p=6
#indica si aun hay movimiento por la ultima interaccion con la particula
movimientos=0
#estado inicil delsistema
ss = zeros(2 * N)
#pociciones iniciales de las masas
def posInicial(ss):
    ss = zeros(2 * N)
    ss[0] = 1.0
    if N == 2:
        ss[1] = -1.0  # modo normal
    if N == 3:
        ss[1] = -1.0 * sqrt(2)
        ss[2] = +1.0
    return ss

ss=posInicial(ss)

display(title='Sistema masa resorte para N masas',y=10,width=1200,height=200)
display(title='Posiciones vs Valocidad',y=250,width=1200)

piso = box(pos=(ss[1]+p,-1,0),length=p*N,height=0.1,width=2,material=materials.wood)


masas=[]
pariculas=[]
posIni=[]
resortes=[]
graficas=[]
for i in range(0,N):
    pAux = p * i
    col = color.magenta
    if i==1: col=color.orange
    if i==2: col=color.blue
    masas.append(sphere(pos=(ss[i]+pAux,0,0),color=col))
    posIni.append(ss[i]+pAux)#almacena las posiciones iniciales de las masas
    graficas.append(gcurve(color=col))
    if i<N-1:
        resortes.append(helix(pos=(ss[i],0,0),length=p/2,color=color.green,radius=0.3,thickness=0.3/5,coils=10.0))

pariculas.append(sphere(pos=(-8.0, 0, 0), color=color.cyan,radius=0.3))
#funcion grafica por definir
def graficar(ss):
    #print ss[0], ss[1], ss[2]
    for i in range(0,N):
        graficas[i].plot(pos=(ss[i],ss[N+i]))
#animacion de la s masas y los resortes
def animar(ss):
    for i in range(0, N):
        pAux = p*i
        masas[i].x = ss[i]+pAux
        if i < N - 1:
            resortes[i].x=ss[i]+pAux
            resortes[i].length=p+float(ss[i+1])-float(ss[i])
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
def interactua(ss):
    global movimientos
    global pariculas
    mueve=False
    golpea=False
    for i in range(0,len(pariculas)):
        if(pariculas[i].x>=0):
            golpea=True
    if(golpea):
        num=randint(0,200)
        if(num==9):
            mueve=True
            movimientos+=1
            print 'se mueve'
    return mueve
#determina si aun se esta moviendo las masas a causa de la ineraccion con la particula
def seMueve(ss):
    global movimientos
    mueve=False
    if(movimientos>0 and pariculas[0].x>p*N-1):
        movimientos-=1
    if(movimientos>0): mueve=True
    return mueve
#crea las pariculas
def newParticula():
    global  pariculas
    if(pariculas[len(pariculas)-1].x>5):
        pariculas.append(sphere(pos=(-8.0, 0, 0), color=color.cyan,radius=0.3))
#elimina las pariculas
def deleteParticula():
    global  pariculas
    if(pariculas[0].x>p*N):
        pariculas[0].color=color.black
        pariculas.pop(0)
#anima las particulas
def animarPArticula():
    global pariculas
    for i in range(0, len(pariculas)):
        pariculas[i].x+=h

#ciclo wile que actualiza la grafica, la animacion y variables
while 1:
    rate(80)
    print movimientos
    graficar(ss)
    newParticula()
    animar(ss)
    animarPArticula()
    if (interactua(ss) or seMueve(ss)):
        ss = rk4(ss)
    deleteParticula()
