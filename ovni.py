t = int(input())
for i in range(t):
    medidas = [int(x) for x in input().split()]
    plat = medidas[-1]
    soma = sum(medidas[:-1])
    if soma <= plat:
        print("CABE!", end="" if i == t-1 else "\n")
    else:
        print("NAO CABE!", end="" if i == t-1 else "\n")