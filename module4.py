def decor(spea):
    def wrapper(v,v0,t):
        spea(v,v0,t)
        print(v0*t+(((v-v0)/t)*t*t)/2)
    return wrapper
@decor
def spead(V,V0,T):
    A=float((V-V0)/T)
    print(A)
try:
    v =int(input())
    v0=int(input())
    t =int(input())
    spead(v,v0,t)
except (AttributeError,ZeroDivisionError):
    print("некорректные данные")

