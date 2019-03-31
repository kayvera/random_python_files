motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda') #adds to end of the list 
print(motorcycles)

motorcycle_2 = []
motorcycle_2.append('honda')
motorcycle_2.append('ducati')
motorcycle_2.append('yamaha')
print(motorcycle_2)

motorcycle_2.insert(0,'suzuki')
print(motorcycle_2)

del motorcycle_2[0] #delete an item from a list
print(motorcycle_2)

popped_motorcycle = motorcycle_2.pop()
print(motorcycle_2)
print(popped_motorcycle)


