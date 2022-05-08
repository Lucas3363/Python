
#fatorial

def fatorial(n):
    if n== 0:
        return 1
    else:
        return n*fatorial(n-1)

print (f"Exercício 1 =", fatorial(5))

#fibonacci

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print (f"Exercício 2 =", fib(6))

#MDC

def mdc(x,y):
    if x == y:
        return x
    elif x < y:
        return mdc(y,x)
    else:
        return mdc(x-y,y)

print(f"Exercício 3 = mdc(64,14) = {mdc(64,14)}")

#SOMA

def soma(m,n):
    if n == m:
        return m
    elif m < n:
        return soma(m,n-1)+n

print(f"Exercício 4 =", soma(10,15))

#SOMA2

def soma(m,n):
    if n == m:
        return m
    elif m < n:
        return m+soma(m+1,n)

print(f"Exercício 5 = soma(10,15) = {soma(10,15)}",f" soma(1,10) = {soma(1,10)}")

#Numero Inteiro

def dig(n):
    if abs(n) <= 9:
        return 1
    elif abs(n) > 9:
        return 1 + dig(n/10)
    
print(f"Exercício 6 = dig(53223) = {dig(53223)}",f" dig(100011) = {dig(100011)}")

#ELEVADO

def pot(x,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1/pot(x,abs(n))
    elif n > 0:
        return x*pot(x,n-1)

print(f"Exercício 7 = pot(2,5) = {pot(2,5)}",f" pot(3,4) = {pot(3,4)}")