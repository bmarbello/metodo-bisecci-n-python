# importar las librerias necesarias
from math import e

# En el metodo f(x) se inserta la función a calcular
def f(x):
  #resultado = ((667.4/x)*(1 - e ** (-0.146*x)))-40
  resultado = x**10-1
  return resultado;

#metodo de bisección
def Bisect(xl, xu, es, imax):
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
def FalsePos(xl, xu, es, imax):
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


# llamada a la función del metodo bisección o falsa posición
print(Bisect(0, 1.3, 0, 5))