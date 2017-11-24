from visual.graph import *

h  =  0.05
t  =  0.0
k  =  1.0
ka =  1.0
m  =  1.0
F0 = 1.0 

ss=array([1.0,1.0,0.0,0.0])#ss[0],ss[1],v1,v2
M=array([[0,0,1,0],[0,0,0,1],[2,1,0,0],[1,2,0,0],])

display(width=1200,height=300,title="Sistema masa-resorte acoplado")
piso      = box(pos=(0,-1,0),length=18,height=0.1,width=2,material=materials.wood)
pared_izq = box(pos=(-9-.05,0,0),length=0.1,height=2,width=2,material=materials.wood)
pared_der = box(pos=(9+.05,0,0),length=0.1,height=2,width=2,material=materials.wood)
masa1     = sphere(pos=(-3,0,0),color=color.red)
masa2     = sphere(pos=(3,0,0),color=color.green)
resorte1  = helix(pos=(-9,0,0),length=5,color=color.blue,radius=0.3,thickness=0.3/5,coils=10.0)
resorte2  = helix(pos=(-2,0,0),length=4,color=color.blue,radius=0.3,thickness=0.3/5,coils=10.0)
resorte3  = helix(pos=(4,0,0),length=5,color=color.blue,radius=0.3,thickness=0.3/5,coils=10.0)

gdisplay(width=1200,height=300,y=325,ymin=-3.0,ymax=3.0,title='Movimiento de las masas 1 y 2 vs tiempo', xtitle='t, s', ytitle='Desplazamiento')
possx1=gcurve(color=color.red)
possx1.plot(pos=(0,2))
possx2=gcurve(color=color.green)

def f(t,ss):
    return dot(M,ss)

def rk4(t,ss):
    k1=h*f(t,ss)
    k2=h*f(t+h/2,ss+k1/2)
    k3=h*f(t+h/2,ss+k2/2)
    k4=h*f(t+h,ss+k3)
    return ss+(k1+2*k2+2*k3+k4)/6

while 1:
	rate(100)
	print t,ss[0],ss[0]-2*cos(t)
	masa1.x=ss[0]-3
	masa2.x=ss[1]+3
	resorte2.x=ss[0]-2
	resorte3.x=ss[1]+4
	resorte1.length=5+float(ss[0])
	resorte2.length=4+float(ss[1])-float(ss[0])
	resorte3.length=5-float(ss[1])

	possx1.plot(pos=(t,ss[0]))
	possx2.plot(pos=(t,ss[1]))
	ss = rk4(t, ss)
	
	t+=h
