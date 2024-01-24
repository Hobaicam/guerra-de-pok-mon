import random

jugador = [100, 100] # Jugador: [PS, defensa]
oponente = [100, 0] # Oponente: [PS, defensa]


# Ataques: [nombre, daño, efecto]
ataques = [ ["malicioso", 0, 10], 
           ["placaje", 35, 0],
           ["ascuas", 20, 0]
]
while jugador[0] > 0 and oponente[0] > 0:
    ataque_jugador = input ("ataque: ").lower()
    ataque_encontrado = None
    for ataque in ataques:
        if ataque[0] == ataque_jugador:
            ataque_encontrado = ataque
            break

    if ataque_encontrado:
        oponente[1] -= ataque_encontrado[2]
        if oponente <= 0:
            oponente[1]=1
        oponente[0] -= ataque_encontrado[1] / (oponente[1]/100)
    else:
        print("Cuidado, tus ataques son malicioso,placaje y ascuas")

    #Turno del Oponente
    ataque_oponente = random. choice (ataques)
    if ataque_oponente[2] > 0:
        jugador [1] -= ataque_oponente[2]
        if jugador[1] <= 0:
            jugador [1] = 1

    jugador [0] = ataque_oponente[1] * (100 / jugador[1])

if oponente [0] <= 0:
    print(" ¡Felicidades, has ganado!") 
else:
    print ("Lo siento, has perdido.")
