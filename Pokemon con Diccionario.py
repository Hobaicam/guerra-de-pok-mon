import random

jugador = [100, 100] # Jugador: [PS, defensa]
oponente = [100, 0] # Oponente: [PS, defensa]


# Ataques: [nombre, daño, efecto]
ataques = [ {"nombre": "malicioso", "daño": 0, "efecto": 10}, 
           {"nombre": "placaje", "daño": 35, "efecto": 0},
           {"nombre": "ascuas", "daño": 20, "efecto": 0}
]
ataques_oponente = [ {"nombre": "látigo", "daño": 0, "efecto": 10}, 
           {"nombre": "placaje", "daño": 35, "efecto": 0},
           {"nombre": "pistola de agua", "daño": 40, "efecto": 0}
]
print("---BIENVENIDO AL JUEGO---")
while jugador[0] > 0 and oponente[0] > 0:
    
    while True: 
        print("\nTÚ TURNO\n")
        ataque_jugador = input ("Elige tú ataque (malicioso, placaje o ascuas): ").lower()
        ataque_encontrado = None
        for ataque in ataques:
            if ataque["nombre"] == ataque_jugador:
                ataque_encontrado = ataque       

        if ataque_encontrado["nombre"]=="malicioso":
            if oponente[1]>0:
                oponente[1]-=ataque_encontrado["efecto"]
                if oponente[1]<=0:
                    oponente[1]=0
                    print("El oponente se quedó sin defensa!")
                    print(f"El PS del oponente es: {oponente[0]}\nLa defensa del oponente es: {oponente[1]}")
                    break
            else:
                print("El oponente no tiene defensa actualmente")
                print(f"El PS del oponente es: {oponente[0]}\nLa defensa del oponente es: {oponente[1]}")
                break
            

        elif ataque_encontrado["nombre"]=="placaje":
            oponente[0]-=ataque_encontrado["daño"]
            if oponente[0]<=0 and oponente[1]>=0:
                oponente[0]=1
            print(f"El PS del oponente es: {oponente[0]}\nLa defensa del oponente es: {oponente[1]}")
            break

        elif ataque_encontrado["nombre"]=="ascuas":
            oponente[0]-=ataque_encontrado["daño"]
            if oponente[0]<=0 and oponente[1]>=0:
                oponente[0]=1
            print(f"El PS del oponente es: {oponente[0]}\nLa defensa del oponente es: {oponente[1]}")
            break
            
            
        else:
            print("Cuidado, tus ataques son malicioso, placaje y ascuas")

    while True:
        ataque_oponente = random. choice (ataques_oponente)
        print("\nTURNO DEL OPONENTE\n")       

        
        if ataque_oponente["nombre"]=="látigo":
            print("El oponente a utilizado: " + ataque_oponente["nombre"])
            if jugador[1]>0:
                jugador[1]-=ataque_oponente["efecto"]
                if jugador[1]<=0:
                    jugador[1]=0
                    print("El oponente se quedó sin defensa!")
                    print(f"El PS del jugador es: {jugador[0]}\nLa defensa del jugador es: {jugador[1]}")
                    break
            else:
                print("El jugador no tiene defensa actualmente")
                print(f"El PS del jugador es: {jugador[0]}\nLa defensa del jugador es: {jugador[1]}")
                break
            

        elif ataque_oponente["nombre"]=="placaje":
            print("El oponente a utilizado: " + ataque_oponente["nombre"])
            jugador[0]-=ataque_oponente["daño"]
            if jugador[0]<=0 and jugador[1]>=0:
                jugador[0]=1
            print(f"El PS del jugador es: {jugador[0]}\nLa defensa del jugador es: {jugador[1]}")
            break

        elif ataque_oponente["nombre"]=="pistola de agua":
            print("El oponente a utilizado: " + ataque_oponente["nombre"])
            jugador[0]-=ataque_oponente["daño"]
            if jugador[0]<=0 and jugador[1]>=0:
                jugador[0]=1
            print(f"El PS del jugador es: {jugador[0]}\nLa defensa del jugador es: {jugador[1]}")
            break
        

if oponente [0] <= 0:
    print(" ¡Felicidades, has ganado!") 
else:
    print ("Lo siento, has perdido.")

# while jugador[0] > 0 and oponente[0] > 0:
#     ataque_jugador = input ("ataque: ").lower()
#     ataque_encontrado = None
#     for ataque in ataques:
#         if ataque["nombre"] == ataque_jugador:
#             ataque_encontrado = ataque
#             break

#     if ataque_encontrado:
#         oponente[1] -= ataque_encontrado["efecto"]
#         if oponente[0] <= 0:
#             oponente[1]=1
#         oponente[0] -= ataque_encontrado["daño"] / (oponente[1]/100)
        
#     else:
#         print("Cuidado, tus ataques son malicioso,placaje y ascuas")

#     #Turno del Oponente
#     ataque_oponente = random. choice (ataques)
#     if ataque_oponente["efecto"] > 0:
#         jugador [1] -= ataque_oponente["efecto"]
#         if jugador[1] <= 0:
#             jugador [1] = 1

#     jugador [0] = ataque_oponente["daño"] * (100 / jugador[1])