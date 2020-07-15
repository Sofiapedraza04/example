from math import *
import time

def f(x):
    return cos(x)-x

def fplusx(x):
    return cos(x)

def df(x):
    return -sin(x)-1

def g(x):
    return x**3 + 4*x**2 -10

def gplusx(x):
    return x**3 + 4*x**2 + x -10

def dg(x):
    return 3*x**2 + 8*x

def bisection(f,a,b, tol):
    ai,bi=a,b
    while abs(bi-ai)>tol:
        ci = (ai+bi)/2.
        if f(ci)==0:
            return ci
        elif f(ai)*f(ci)<0 :
            bi=ci
        else:
            ai=ci
    return ci

def Regula_Falsi(f,a,b, tol):
    ai,bi=a,b
    while abs(bi-ai)>tol:
        ci = ai - f(ai)*(bi-ai)/(f(bi)-f(ai))
        if f(ci)==0:
            return ci
        elif f(ai)*f(ci)<0 :
            bi=ci
        else:
            ai=ci
    return ci

def Newton_Rapson(f,df,x0, tol):
    xi=x0
    xi_old=x0+100.
    while abs(xi-xi_old)>tol: #while abs(xi)>tol:
        xi_old = xi
        xi = xi - f(xi)/df(xi)
        if f(xi)==0:
            return xi
    return xi

def Secant(f,x0,x1, tol):
    xi=x1
    xi_old=x0
    while abs(xi-xi_old)>tol:
        temp = xi
        xi = xi - f(xi)*(xi_old-xi)/(f(xi_old)-f(xi))
        xi_old = temp
        if f(xi)==0:
            return xi
    return xi
 
def fixed_point(f,x0, tol):
    xi=x0
    xi_old=x0+2*tol
    while abs(xi-xi_old)>tol:
        print(xi)
        xi_old = xi
        xi = f(xi)
    return xi
    
def fixed_point_N(f,x0, tol,N=1000):
    xi=x0
    xi_old=x0+2*tol
    i=0
    while (i<N) and (abs(xi-xi_old)>tol):
        xi_old = xi
        xi = f(xi)
        i+=1
    return xi
    
t1=time.time()
x = bisection(f,0.0,3.14, 1e-4)
t2=time.time()
print("x=%f ... t=%f"%(x,t2-t1))
t1=time.time()
x = Regula_Falsi(f,0.0,3.14, 1e-4)
t2=time.time()
print("x=%f ... t=%f"%(x,t2-t1))
t1=time.time()
x = Newton_Rapson(f,df,0.0, 1e-4)
t2=time.time()
print("x=%f ... t=%f"%(x,t2-t1))
t1=time.time()
x = Secant(f,0.0,0.1, 1e-4)
t2=time.time()
print("x=%f ... t=%f"%(x,t2-t1))
t1=time.time()
x = fixed_point(fplusx,0.0, 1e-4)
t2=time.time()
print("x=%f ... t=%f"%(x,t2-t1))

## What happen with g? why it is better not to use 3.14?
t1=time.time()
x = bisection(g,0.0,2.0, 1e-4)
t2=time.time()
print("x=%f ... t=%f"%(x,t2-t1))
t1=time.time()
x = Regula_Falsi(g,0.0,2.0, 1e-4)
t2=time.time()
print("x=%f ... t=%f"%(x,t2-t1))
## Why it does not work with g?
t1=time.time()
print("dg+1 = ", dg(1.36)+1)
x = fixed_point(gplusx,1.31, 1e-4)
t2=time.time()
print("x=%f ... t=%f"%(x,t2-t1))
