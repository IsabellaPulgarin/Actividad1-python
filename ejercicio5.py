#ejercicio5
print("digita el total a pagar")
num=float(input())
print("que porcentaje de propina quieres dejar: 10 , 15, 20")
tip=str(input())
if tip=="10":
    print(f"el valor de la propina es:{num*(10/100)}")
elif tip=="15":
    print(f"el valor de la propina es:{num*(15/100)}")
elif tip=="20":
    print(f"el valor de la propina es:{num*(20/100)}")
else:
    print("no dejas propina")