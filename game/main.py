#Jueguito de piedra papel tijera
import sys
import random

print("Welcome Welcome \n")

wins_compu=0
wins_user=0

while wins_compu <3 and wins_user<3:
    x=("piedra", "papel", "tijera")
    
    option=input("\n1, 2, 3, Piedra, Papel o Tijera: ")
    option=option.lower()
    if not option in x:
      sys.exit("Tu opcion no es valida")
    else:
      print("\nDecidiste jugar: ", option)
    
    
    computer_option=random.choice(x)
    print("\nLa computadora elige: ", computer_option, "\n")
    
    if option==computer_option:
      print("Empate")
    elif option=="piedra":
      if computer_option=="papel":
        print("Punto para la compu")
        wins_compu +=1
      else:
        print("Punto para el usuario")
        wins_user+=1
    elif option=="papel":
      if computer_option=="tijera":
        print("Punto para la compu")
        wins_compu +=1
      else:
        print("Punto para el usuario")
        wins_user+=1
    elif option=="tijera":
      if computer_option=="piedra":
        print("Punto para la compu")
        wins_compu +=1
      else:
        print("Punto para el usuario")
        wins_user+=1
    print(f"\nComputer => {wins_compu}") 
    print(f"\nUser => {wins_user}") 
    if wins_compu == 3:
      print(f"\nCOMPUTER WINS")
    elif wins_user == 3:
      print(f"\nUSER WINS")
    else:
      continue

    