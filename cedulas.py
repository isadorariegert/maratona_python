troco = int(input())
print(f'{troco//100} nota(s) de R$ 100')
troco = troco%100
print(f'{troco//50} nota(s) de R$ 50')
troco = troco%50
print(f'{troco//20} nota(s) de R$ 20')
troco = troco%20
print(f'{troco//10} nota(s) de R$ 10')
troco = troco%10
print(f'{troco//5} nota(s) de R$ 5')
troco = troco%5
print(f'{troco//2} nota(s) de R$ 2')
troco = troco%2
print(f'{troco//1} nota(s) de R$ 1', end="")
