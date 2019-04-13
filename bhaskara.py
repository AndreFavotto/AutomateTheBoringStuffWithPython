a = eval(input('Digite o coeficiente a: '))
b = eval(input('Digite o coeficiente b: '))
c = eval(input('Digite o coeficiente c: '))

delta = b**2 -4*a*c
if (delta>0):
    x1 = (b*-1 + delta**(1/2))/(2*a)
    x2 = (b*-1 - delta**(1/2))/(2*a)
    print('x1={:.3f} , x2={:.3f}'.format(x1,x2))
elif (delta<0):
    x1r = b*(-1)/2*a
    x1i =((delta*(-1))**(1/2))/(2*a)
    x2r = b*(-1)/2*a
    x2i = ((delta*(-1))**(1/2))/(2*a)
    print('x1={:.3f} + {:.3f}i, x2={:.3f} - {:.3f}i'.format(x1r,x1i,x2r,x2i))
else:
    x1 = (b*-1/2*a)
    print('x={:.3f}'.format(x1))
