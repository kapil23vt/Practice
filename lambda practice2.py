list = [(10,4),(20,3),(40,1),(30,2)]
h = lambda x:x[1]

list.sort(key = h)

print(list) # [(40, 1), (30, 2), (20, 3), (10, 4)]

