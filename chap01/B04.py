N = input()
while len(N) < 8:
    N = '0'+ N

sum = 0
for i in range(7,-1,-1): 
    sum += 2**i * int(N[7-i])
print(sum)
