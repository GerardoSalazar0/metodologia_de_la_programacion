"""
    Slicing a list
"""
players= ['charles', 'martina', 'florence', 'eli']
print("Lista original:", players)
print("Slicing", players[0:3]) #indice de donde hasta donde 0, 1 y 2

print("Slice:", players[1:4])
print("Slice:", players[:4])
print("Slice:", players[:2])
print("Slice:", players[-3:])
print("Slice:", players[:-3])
print("Slice:", players[:-4])
print("Slice:", players[5:])


# Slicing en un for 
players= ['charles', 'martina', 'florence', 'eli']
print("Los primeros tres jugadores son:")
for player in players[0:3]:
    print(player.title())


# Copiar una lista
players= ['charles', 'martina', 'florence', 'eli']
# player_2=players ERROR WE
player_2=players[:]
player_2= list(players)
players_3= players.copy()


cars = ["bwm", "toyota", "volkswagen", "porche"]
print(cars)
cars[0] = "bmw"
cars[3] = "porshe"
print(cars)

