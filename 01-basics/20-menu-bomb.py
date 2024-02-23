import time
# Agregar un menú de 2 opciones para ver la bomba de tiempo
# 1 ver bomba de tiempo 2 para salir

def boom():
    num = 10
    while (num >= 0):
      print(num)
      time.sleep(1)
      num = num - 1
    print("Boom")

while True:
  try:
    print("escoje entre las siguientes opciones 1 - ver bomba / 2- salir")
    user=int(input("Ingrese su eleccion: "))
    if user <1 or user > 2:
      print("Ingrese una opcion valida 1/2")
    elif user == 1:
      boom()
    else:
      print("Hasta luego")
      break
  except ValueError:
    print("Ingrese una opcion valida.")
    continue
