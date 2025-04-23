#ejercicio8
print("Digite su peso en kilogramos: ")
weight=float(input())
print("Digite su altura en metros: ")
height=float(input())
imc=(weight/(height*height))

if imc<18.5:
    print("Bajo de peso")
elif imc>=18.5 and imc<= 24.9:
    print("Normal")
elif imc>29.9:
    print("Obesidad")
else:
    print("Sobrepeso")