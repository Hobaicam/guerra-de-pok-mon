import random

#PS es puntos en salud
jugador = [100, 100]  # Jugador: [PS, defensa]
oponente = [100, 0]  # Oponente: [PS, defensa]

# Ataques: [nombre, daño, efecto]
ataques = [
    ["malicioso", 10],
    ["placaje", 35],
    ["ascuas", 20]
]

while jugador[0] > 0 and oponente[0] > 0:
    ataque_jugador = input("ataque: (malicioso, placaje, ascuas): ").lower()
    ataque_encontrado = None
    for ataque in ataques:
        if ataque[0] == ataque_jugador:
            ataque_encontrado = ataque
            break

    if ataque_encontrado:
        oponente[1] -= ataque_encontrado[1]
        if oponente[1] <= 0:
            oponente[1] = 1  # Defensa mínima
        oponente[0] -= int(ataque_encontrado[1] / (oponente[1] / 100))
    else:
        print("Ataque no válido. Los ataques disponibles son: malicioso, placaje, ascuas")

# Verificar si el oponente ha sido derrotado
    if oponente[0] <= 0:
        print("¡Felicidades, has ganado!")
        break
               
# Turno del oponente
    ataque_oponente = random.choice(ataques)
    jugador[1] -= ataque_oponente[1]
    if jugador[1] <= 0:
        jugador[1] = 1  # Defensa mínima
    jugador[0] -= int(ataque_oponente[1] / (jugador[1] / 100))

# Verificar si el jugador ha sido derrotado
if jugador[0] <= 0:
    print("Lo siento, has perdido.")
