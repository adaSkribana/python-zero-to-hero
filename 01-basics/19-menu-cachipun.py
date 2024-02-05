import random
# Crear un juego con cachipún y un menú de opciones
# La opción número 1 será jugar y la opción 2 salir

menu_option = 0
name_user = input("Para comenzar, ¿como quieres que te llame? :")
while menu_option != 2: # mientras menu_option sea distinto a 2
    menu_option = int(input("Ingresa 1 para jugar o 2 para salir"))
    if menu_option == 1:
        print("Jugemos 'piedra', 'papel' o 'tijeras' :D !!!")

        computer_choice = random.choice([ "piedra", "papel","tijeras"])
        user_option = input("escoge entre las siguientes expresiones: 'piedra', 'papel' o 'tijeras' :")

        if computer_choice == user_option:
            print(f"{name_user} Hemos empatado! ")
        elif computer_choice== "piedra" and user_option =="papel" or computer_choice =="papel" and user_option =="tijeras" or computer_choice =="tijeras" and user_option =="piedra":
            print(f"{name_user} Me haz vencido!")
        elif computer_choice== "piedra" and user_option =="tijeras" or computer_choice =="papel" and user_option =="piedra" or computer_choice =="tijeras" and user_option =="papel":
            print(f"{name_user} Haz sido vencid@!")
        else:
            print(f"{name_user} Ingresa una de las expresiones mencionadas.")
