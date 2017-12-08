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
#efinicion de arreglos
masas=[]
pariculas=[]
resortes=[]
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

display(title='Interaccion de particulas cuanticas',y=10,width=1200)

piso = box(pos=(ss[1]+p,-1,0),length=p*N,height=0.1,width=2,material=materials.wood)
#se crea la primera esfera
pariculas.append(sphere(pos=(-9.0, 0, 0), color=color.red,radius=0.4))
#se crea la figura conica de donde saldran las particulas
cono=cone(pos=(-8.0,0,0),axis=(-4.0,0,0),color=color.orange,radius=1)
#se inicializan las masas y los resortes
for i in range(0,N):
    pAux = p * i
    col = color.blue
    if i==1: col=color.cyan
    if i==2: col=color.green
    masas.append(sphere(pos=(ss[i]+pAux,0,0),color=col))
    if i<N-1:
        resortes.append(helix(pos=(ss[i],0,0),length=p/2,color=color.white,radius=0.3,thickness=0.3/5,coils=10.0))

#animacion de las masas y los resortes
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
'''
___________________________________________________________________________
----------------------definicion de funciones------------------------------

'''
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
    posPart=-1;
    for i in range(0,len(pariculas)):
        if(pariculas[i].x>=masas[1].x-masas[1].radius and pariculas[i].x<=masas[1].x+masas[1].radius):
            golpea=True
            posPart=i
            print 'golpea'
    if(golpea):
        num=randint(0,200)
        print 'NomR', num
        if 9 == num or 24 == num or 18 == num or 74 == num:
            mueve=True
            movimientos+=1
            print 'se mueve'
    return mueve
#determina si aun se esta moviendo las masas a causa de la ineraccion con la particula
def seMueve(ss):
    global movimientos
    mueve=False
    if(movimientos>0 and pariculas[0].x>p*N-0.9):
        movimientos-=1
    if(movimientos>0): mueve=True
    return mueve
#crea las pariculas
def newParticula():
    global  pariculas
    if(pariculas[len(pariculas)-1].x>-3):
        pariculas.append(sphere(pos=(-9.0, 0, 0), color=color.red,radius=0.4))
#elimina las pariculas
def deleteParticula():
    global  pariculas
    if(pariculas[0].x>p*N-0.35):
        pariculas[0].color=color.black
        pariculas.pop(0)
#anima las particulas
def animarParticula():
    global pariculas
    for i in range(0, len(pariculas)):
        pariculas[i].x+=h

#ciclo wile que actualiza la grafica, la animacion y variables
while 1:
    rate(80)
    print movimientos
    newParticula()
    animar(ss)
    animarParticula()
    if (interactua(ss) or seMueve(ss)):
        ss = rk4(ss)
    deleteParticula()
