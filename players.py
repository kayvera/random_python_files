players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #prints the first 3
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-2:]) #starts at the end of the list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print("\t" + player.title())



