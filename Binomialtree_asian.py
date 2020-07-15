from math import exp, sqrt
import time

def V(t,T,S,A,u,d,p,r,K):
    if(t==T):
        value = max(A-K,0)
    else:
        value = ((p*V(t+1,T,u*S, ((t+1)*A+u*S)/(t+2),u,d,p,r,K)+(1-p)*V(t+1,T,d*S,((t+1)*A+d*S)/(t+2) ,u,d,p,r,K)))/(1+r)
    return value

def binomial_Asian(T,S,u,d,r,K):
    if (d < 1+r) and (1+r < u):
        p = (1+r-d)/(u-d)
    else:
        print ("No risk Neutral measure, change the parameters")
        return -1
    return V(0,T,S,S,u,d,p,r,K)

u = exp(0.3*sqrt(1./12))
d = 1./u
for i in range(1):
    t0=time.clock()
    BA = binomial_Asian(3,40.,u,d,0.05,39)
    t1=time.clock()
    print ("%d> %f --- elapsed time: %f"%(i,BA,t1-t0))
	
