from visual.graph import *

h  =  0.05
t  =  0.0
L  =  1.0
x1 =  L
v1 =  0.0
x2 =  0.0
v2 =  0.0
k  =  1.0
ka =  0.1
m  =  1.0

display(width=1000,height=300,title="Sistema masa-resorte acoplado")
piso      = box(pos=(0,-1,0),length=18,height=0.1,width=2,material=materials.wood)
pared_izq = box(pos=(-9-.05,0,0),length=0.1,height=2,width=2,material=materials.wood)
pared_der = box(pos=(9+.05,0,0),length=0.1,height=2,width=2,material=materials.wood)
masa1     = sphere(pos=(-3,0,0),color=color.red)
masa2     = sphere(pos=(3,0,0),color=color.green)
resorte1  = helix(pos=(-9,0,0),length=5,color=color.blue,radius=0.3,thickness=0.3/5,coils=10.0)
resorte2  = helix(pos=(-2,0,0),length=4,color=color.blue,radius=0.3,thickness=0.3/5,coils=10.0)
resorte3  = helix(pos=(4,0,0),length=5,color=color.blue,radius=0.3,thickness=0.3/5,coils=10.0)

gdisplay(width=1200,height=300,y=325,ymin=-3.0,ymax=3.0,title='Movimiento de las masas 1 y 2 vs tiempo', xtitle='t, s', ytitle='Desplazamiento')
x1graph=gcurve(color=color.red)
x1graph.plot(pos=(0,2))
x2graph=gcurve(color=color.green)

def f1(t,x1,v1,x2,v2):
	return -k/m*x1+ka/m*(x2-x1)
def g1(t,x1,v1,x2,v2):
	return v1

def f2(t,x1,v1,x2,v2):
	return -k/m*x2-ka/m*(x2-x1)
def g2(t,x1,v1,x2,v2):
	return v2

while 1:
	rate(40)

	masa1.x=x1-3
	masa2.x=x2+3
	resorte2.x=x1-2
	resorte3.x=x2+4
	resorte1.length=5+x1
	resorte2.length=4+x2-x1
	resorte3.length=5-x2

	x1graph.plot(pos=(t,x1))
	x2graph.plot(pos=(t,x2))

	k1=h*f1(t,x1,v1,x2,v2)
	l1=h*g1(t,x1,v1,x2,v2)
	m1=h*f2(t,x1,v1,x2,v2)
	n1=h*g2(t,x1,v1,x2,v2)

	k2=h*f1(t+h/2,x1+l1/2,v1+k1/2,x2+n1/2,v2+m1/2)
	l2=h*g1(t+h/2,x1+l1/2,v1+k1/2,x2+n1/2,v2+m1/2)
	m2=h*f2(t+h/2,x1+l1/2,v1+k1/2,x2+n1/2,v2+m1/2)
	n2=h*g2(t+h/2,x1+l1/2,v1+k1/2,x2+n1/2,v2+m1/2)

	k3=h*f1(t+h/2,x1+l2/2,v1+k2/2,x2+n2/2,v2+m2/2)
	l3=h*g1(t+h/2,x1+l2/2,v1+k2/2,x2+n2/2,v2+m2/2)
	m3=h*f2(t+h/2,x1+l2/2,v1+k2/2,x2+n2/2,v2+m2/2)
	n3=h*g2(t+h/2,x1+l2/2,v1+k2/2,x2+n2/2,v2+m2/2)

	k4=h*f1(t+h,x1+l3,v1+k3,x2+n3,v2+m3)
	m4=h*f2(t+h,x1+l3,v1+k3,x2+n3,v2+m3)
	l4=h*g1(t+h,x1+l3,v1+k3,x2+n3,v2+m3)
	n4=h*g2(t+h,x1+l3,v1+k3,x2+n3,v2+m3)

	v1+=k1/6+k2/3+k3/3+k4/6
	v2+=m1/6+m2/3+m3/3+m4/6
	x1+=l1/6+l2/3+l3/3+l4/6
	x2+=n1/6+n2/3+n3/3+n4/6
	t+=h
