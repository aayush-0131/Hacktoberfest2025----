y = int(input())
y += 1  # start from the next year
 
while len(set(str(y))) != 4:
    y += 1
 
print(y)
