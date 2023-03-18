# importar las librerias necesarias
from math import e, pi

#calcular es
def es(n):
   numero = (0.5*10**(2-n));
   return numero;

# En el metodo f(x) se inserta la función a calcular
def f(x):
  resultado = x**10-1;
  return resultado;

#metodo de bisección
def Bisect(xl, xu, es, imax = 100):
  #inicializar variables
    iter = 0
    xr = 0
    ea = 100
  #iniciarlizar las iteraciones
    while True:
      #hallar xr
        xrold = xr
        xr = (xl + xu)/2
        iter = iter + 1

      #calcular el EA
        if xr != 0:
            #et = abs((14.7802 - xr)/14.7802)*100
            ea = abs((xr - xrold)/xr)*100
            #Muestra en consola los valores que toman las variables en cada iteración
            print("iteración: ",iter,"XL: ",xl,"XU: ",xu,"XR: ",xr,"ea: ",ea);

        test = f(xl) * f(xr)
       #Definir quien va a ser el nuevo xu o xr
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
       #si el ea es menor al es o el numero iteraciones supera las iteraciones maximas se sale del ciclo
        if ea < es or iter > imax:
            break
    #retorna el resultado obtenido en terminos de xr
    return xr

#metodo de falsa posición
def FalsePos(xl, xu, es, imax = 100):
  #inicializar variables
  xr = 0
  ea = 100
  iter = 0
  #iniciarlizar las iteraciones
  while True:
    #hallar xr nuevo
    xrold = xr
    xr = xu -   ((f(xu)*(xl-xu))/(f(xl)-f(xu)));
    iter = iter + 1
    #calcular el EA
    if xr != 0:
      # et = abs((5.60979 - xr)/5.60979)*100
      ea = abs((xr - xrold)/xr)*100
      #Muestra en consola los valores que toman las variables en cada iteración
      print("iteración: ",iter,"XL: ",xl,"XU: ",xu,"XR: ",xr,"ea: ",ea);
    
    test = f(xl) * f(xr)
    #Definir quien va a ser el nuevo xu o xr
    if test < 0:
      xu = xr
    elif test > 0:
      xl = xr
    else:
      ea = 0

    #si el ea es menor al es o el numero iteraciones supera las iteraciones maximas se sale del ciclo
    if ea < es or iter > imax:
      break
  #retorna el resultado obtenido en terminos de xr
  return xr




  #metodo de la falsa posición modificada

def ModFalsePos(xl, xu, es, imax=100):
    iter = 0
    fl = f(xl)
    fu = f(xu)
    il = 0
    iu = 0
    xr = 0
    ea = 100
    
    while True:
        xrold = xr
        xr = xu - fu * (xl - xu) / (fl - fu)
        fr = f(xr)
        iter += 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
            print("iter: ",iter,"xl: ",xl,"xu: ",xu,"xr: ",xr,"ea: ",ea)
        test = fl * fr
        if test < 0:
            xu = xr
            fu = f(xu)
            iu = 0
            il += 1
            if il >= 2:
                fl /= 2
        elif test > 0:
            xl = xr
            fl = f(xl)
            il = 0
            iu += 1
            if iu >= 2:
                fu /= 2
        else:
            ea = 0
        
        if ea < es or iter >= imax:
            break
    
    return xr


# llamada a la función del metodo bisección o falsa posición
print(ModFalsePos(0, 1.3, 0.05,10))