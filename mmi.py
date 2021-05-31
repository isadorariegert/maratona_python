t = int(input())
for i in range(t):
    notas = [int(x) for x in input().split()]
    nota_min = int(min(notas))
    nota_max = int(max(notas))
    print(nota_min, nota_max)
    if nota_min == nota_max:
        print("S", end="" if i == t-1 else "\n")
    else:
        print("N", end="" if i == t-1 else "\n")