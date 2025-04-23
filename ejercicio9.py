#ejercicio9
print("Digite un año")
year=int(input())

if year%4==0 and year%100==0:
    print("El año si es bisiesto")
elif year%400==0:
        print("El año si es bisiesto")
else:
      print("El año no es bisiesto")        