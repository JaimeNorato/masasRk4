from visual.graph import *
#1 masa matris 2*2
h=0.05
t=0.0
m=1.0
k=1.0
b=0.1

ss=array([2.0,0.0])#estado del sistema
#M=array([[0.0,1.0],[-k/m,-b/m]])#para amortiguado se agrega -b/m -> para normal se deja en 0

M=array([[0.0,1.0],[-k/m,0.0]])#para amortiguado se agrega -b/m -> para normal se deja en 0

display(title='Oscilador masa-resorte',y=400)
masa=sphere(color=color.red)
resorte=helix(pos=(-6,0,0),length=5,radius=0.5)
posx=gcurve(color=color.red)
velx=gcurve(color=color.blue)

def f(t,ss):
    return dot(M,ss)

def euler(t,ss):
    return ss+h*f(t,ss)

def rk1(t,ss):
    k1=h*f(t,ss)
    return ss+k1

def rk2(t,ss):
    k1=h*f(t,ss)
    k2=h*f(t+h,ss+k1)
    return ss+(k1+k2)/2

def rk4(t,ss):
    k1=h*f(t,ss)
    k2=h*f(t+h/2,ss+k1/2)
    k3=h*f(t+h/2,ss+k2/2)
    k4=h*f(t+h,ss+k3)
    return ss+(k1+2*k2+2*k3+k4)/6
 
while 1:
    rate(100)
   #ss[0]->posicion, ss[1] velocidad
    print t,ss[0],ss[0]-2*cos(t)#,ss[1]
    masa.x=ss[0]
    resorte.length=5+float(ss[0])
    posx.plot(pos=(t,ss[0]))
    velx.plot(pos=(t,ss[1]))

    ss=rk4(t,ss)
    t=t+h
