import random

numero_secreto=random.randint(1,20)
intentos_restantes=5
print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un numero del 1 al 20.")

while intentos_restantes > 0:
    print("Tienes",intentos_restantes,"intentos restantes.")
    try:
        adivinanza=int(input("introduce tu adivinanza:"))
        
        if adivinanza < 1 or adivinanza > 20:
            print("Por favor, introduce un numero entre 1 y 20.")
            
            continue
        
        if adivinanza < numero_secreto:
            print("El numero secreto es mayor.")
        elif adivinanza > numero_secreto:
            print("El numero secreto es menor.")
        else:
            print(f"¡Felicidades! adivinaste el numero secreto",numero_secreto)
            break
        
        intentos_restantes -= 1
        
        print("Por favor, introduce un numero valido.")
            
        if intentos_restantes == 0:
            print("Lo siento, se te acabaron los intentos. El numero secreto era ,{numero_secreto}")