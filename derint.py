import sympy as sp
a=int(raw_input("enter coefficient of x raised to power b"))
b=int(raw_input("enter coefficient of x raised to power b"))
c=int(raw_input("enter coefficient of x raised to power b"))
d=int(raw_input("enter coefficient of x raised to power b"))
e=int(raw_input("enter coefficient of x raised to power b"))
x=sp.Symbol('x')

print (sp.diff(a*x**5+b*x**4+c*x**3+d*x**2+e*x**1+1,x))

print (sp.integrate(a*x**5+b*x**4+c*x**3+d*x**2+e*x**1+ 1,x))
    
