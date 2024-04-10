inputvalor = int(input())

white = True
whites = 0
blacks = 0

for i in range(inputvalor):
    for j in range(inputvalor):
        if white:
            white = False
            whites += 1
        else:
            white = True
            blacks +=1 

print(f"{whites} casas brancas e {blacks} casas pretas")
