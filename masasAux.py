from PyQt5.uic.Compiler.qtproxies import i18n_string
from visual.graph import *

h  =  0.1
t  =  0.0
L  =  2.0
#posiciones y velocidades de las masas
x1 =  L
v1 =  0.0
x2 =  0.0
v2 =  0.0
x=[L,]
v=[0.0,]
k1=[0.0,]
l1=[0.0,]
k2=[0.0,]
l2=[0.0,]
k3=[0.0,]
l3=[0.0,]
k4=[0.0,]
l4=[0.0,]
#constatnte elastica y masa
k  =  1.0
ka =  1.0
m  =  1.0
#Masas
nMasas=2;
masas=[]
p=-3

display(width=1200,height=300,title="Sistema masa-resorte acoplado")
piso      = box(pos=(0,-1,0),length=18,height=0.1,width=2,material=materials.wood)
pared_izq = box(pos=(-9-.05,0,0),length=0.1,height=2,width=2,material=materials.wood)
pared_der = box(pos=(9+.05,0,0),length=0.1,height=2,width=2,material=materials.wood)
#Masas
pAux=p
for i in range(0,nMasas):
	col = color.red
	if i%2==0:
		col=color.green
	if i%3==0:
		col=color.cyan
	masas.append(sphere(pos=(pAux,0,0),color=col))
	pAux=3*i
	#inicializand x y v
	if i>0:
		x.append(0.0)
		v.append(0.0)
		k1.append(0.0)
		l1.append(0.0)
		k2.append(0.0)
		l2.append(0.0)
		k3.append(0.0)
		l3.append(0.0)
		k4.append(0.0)
		l4.append(0.0)

#masa1     = sphere(pos=(-3,0,0),color=color.red)
#masa2     = sphere(pos=(3,0,0),color=color.green)
#Resortes
resorte1  = helix(pos=(-9,0,0),length=5,color=color.blue,radius=0.3,thickness=0.3/5,coils=10.0)
resorte2  = helix(pos=(-2,0,0),length=4,color=color.blue,radius=0.3,thickness=0.3/5,coils=10.0)
resorte3  = helix(pos=(4,0,0),length=5,color=color.blue,radius=0.3,thickness=0.3/5,coils=10.0)

gdisplay(width=1200,height=300,y=325,ymin=-3.0,ymax=3.0,title='Movimiento de las masas 1 y 2 vs tiempo', xtitle='t, s', ytitle='Desplazamiento')
x1graph=gcurve(color=color.red)
x1graph.plot(pos=(0,2))
x2graph=gcurve(color=color.green)

def f1(x,x1,x2,ka):
	return -k/m*x+ka/m*(x2-x1)

def g1(v1):
	return v1

while 1:
	rate(40)
	#calculo de masas
	pAux=p
	for i in range(0, nMasas):
		print i
		print len(k1)
		if i<(nMasas-1):
			masas[i].x=x[i]+pAux
			pAux=3*i
			# RK4

			k1[i] = h * f1(x[i], x[i], x[i+1], ka)
			k1[i+1] = h * f1(x[i+1], x[i], x[i+1], -ka)
			l1[i] = h * g1(v[i])
			l1[i+1] = h * g1(v[i+1])

			k2[i] = h * f1(x[i] + k1[i+1] / 2, x[i] + k1[i+1] / 2, x[i+1] + l1[i+1] / 2, ka)
			k2[i+1] = h * f1(x[i+1] + l1[i+1] / 2, x[i] + k1[i+1] / 2, x[i+1] + l1[i+1] / 2, -ka)
			l2[i] = h * g1(v[i] + k1[i] / 2)
			l2[i+1] = h * g1(v[i+1] + k1[i+1] / 2)
			'''
			 sigue->
			k3=h*f1(x1+l2/2,x1+l2/2,x2+n2/2,ka)
			m3=h*f2(x2+n2/2,x1+l2/2,x2+n2/2,-ka)
			l3=h*g1(v1+k2/2)
			n3=h*g2(v2+m2/2)
			'''
			k3[i] = h * f1(x[i] + k2[i+1] / 2, x[i] + k2[i+1] / 2, x[i+1] + m2[i+1] / 2, ka)
			m3[i] = h * f1(x[i+1] + m2[i+1] / 2, x[i] + k2[i+1] / 2, x[i+1] + m2[i+1] / 2, -ka)
			k3[i+1] = h * g1(v[i] + k2[i] / 2)
			m3[i+1] = h * g1(v[i+1] + m2[i] / 2)
			'''
			k4=h*f1(x1+l3,x1+l3,x2+n3,ka)
			m4=h*f2(x2+n3,x1+l3,x2+n3,-ka)
			l4=h*g1(v1+k3)
			n4=h*g2(v2+m3)
			'''
			k4[i] = h * f1(x[i] + k3[i+1], x[i] + k3[i+1], x[i+1] + m3[i+1], ka)
			m4[i] = h * f1(x[i+1] + m3[i+1], x[i] + k3[i+1], x[i+1] + m3[i+1], -ka)
			k4[i+1] = h * g1(v[i] + k3[i])
			m4[i+1] = h * g1(v[i+1] + m3[i])

			v[i] += k1[i] / 6 + k2[i] / 3 + k3[i] / 3 + k4[i] / 6
			v[i+1] += k1[i+1] / 6 + k2[i+1] / 3 + k3[i+1] / 3 + k4[i+1] / 6
			x[i] += k1[i+1] / 6 + k2[i+1] / 3 + k3[i+1] / 3 + k4[i+1] / 6

	#masa1.x=x1-3
	#masa2.x=x2+3
	#calculo de resortes
	resorte2.x=x[i]-2
	resorte3.x=x2+4
	resorte1.length=5+x[i]
	resorte2.length=4+x2-x[i]
	resorte3.length=5-x2
	#graficas
	x1graph.plot(pos=(t,x[i]))
	x2graph.plot(pos=(t,x2))
	#fin graficas


	t+=h