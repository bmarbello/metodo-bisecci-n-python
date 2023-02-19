#metodo de bisección pasado a codigo
def Bisect(xl, xu, es, imax, xr, iter, ea):
  iter = 0;
  
  while True:
    
    xrold = xr;
    xr = (xl + xu)/2;
    iter = iter + 1;
    
    if xr != 0:
      ea = abs((xr - xrold)/xr)*100;

    test = xr * xl;

    if test < 0:
      xu = xr;
    elif test > 0:
      xl = xr;
    else:
      ea = 0;
      
    if ea < es or iter > imax:
      break;


  return xr;

  
#llamada a la función del metodo bisección
print(Bisect(12,16,0,4,14,0,0));