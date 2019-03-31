alien_color = 'red'

if alien_color is 'green':
	print("You just earned 5 points!")
else:
	print("Try again next time!")

alien_color = 'green'

if alien_color is 'green':
	print("You just earned 5 points for shooting the alien!")
elif alien_color is 'yellow':
	print("You just earned 10 points for shooting the alien!")
else:
	print("You just earned 15 points for shooting the alien!")
	
alien_color = 'yellow'

if alien_color is 'green':
	print("You just earned 5 points for shooting the alien!")
elif alien_color is 'yellow':
	print("You just earned 10 points for shooting the alien!")
else:
	print("You just earned 15 points for shooting the alien!")

alien_0 = {'color': 'green', 'points':5}

print(alien_0['color'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#alien_0 = {'color': 'green', 'points':5, 'y-position': 25, 'x-position':0}

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color': 'green'}
print('The alien is ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else: 
	#this must be the fast alien
	x_increment = 3

#the new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


alien_0 = {'color': 'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

#make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10 
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15 

#show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
	print("...")

#show how many aliens have been created
print("total number of aliens: " + str(len(aliens)))

	


























