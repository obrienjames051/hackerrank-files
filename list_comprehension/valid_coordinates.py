# this takes inputs x, y, z, and n. Creates a list of all coordinates between [0,0,0] and [x,y,z] where i + j + k != n

x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [[i,j,k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k != n]
#shorter way of writing nested loops

print(coordinates)