from visual.graph import *

N=raw_input('N? ')#numero de masas
if N=='':N=2
N=int(N)

h=0.05
t=0.0
k=1.0
m=1.0
p=6

ss=zeros(2*N)#estado inicil delsistema
ss[0]=1.0
if N==2:
    ss[1]=-1.0#modo normal
if N==3:
    ss[1]=-1.0*sqrt(2)
    ss[2]=+1.0

display(title='Sistema masa resorte para N masas',y=10,width=1200,height=200)
display(title='Posiciones vs Valocidad',y=250,width=1200)

piso = box(pos=(ss[0]+p,-1,0),length=p*N,height=0.1,width=2,material=materials.wood)


masas=[]
resortes=[]
graficas=[]
for i in range(0,N):
    pAux = p * i
    col = color.magenta
    if i%5==0: col=color.red
    if i%3==0: col=color.orange
    if i%2==0: col=color.blue
    masas.append(sphere(pos=(ss[i]+pAux,0,0),color=col))
    graficas.append(gcurve(color=col))
    if i<N-1:
        resortes.append(helix(pos=(ss[i],0,0),length=p/2,color=color.green,radius=0.3,thickness=0.3/5,coils=10.0))


#funcion grafica por definir
def graficar(ss):
    for i in range(0,N):
        print N, i, ss[i],N+i,ss[N+i]
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
#ciclo wile que actualiza la grafica, la animacion y variables
while 1:
    rate(80)
    graficar(ss)
    animar(ss)
    ss = rk4(ss)
