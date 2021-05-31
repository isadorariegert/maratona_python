def calc(op, n1, n2):
    if op == "+":
        return n1+n2
    if op == "-":
        return n1-n2
    if op == "*":
        return n1*n2
    if n2 == 0:
        return "erro"
    return n1//n2

n1 = int(input())
op1 = input()
n2 = int(input())
op2 = input()
n3 = int(input())

try:
    if op1 != "*" and op1 != "/" and (op2 == "*" or op2 == "/"):
        p2 = calc(op2, n2, n3)
        p1 = calc(op1, n1, p2)
        print(p1, end="")
    else:
        p1 = calc(op1, n1, n2)
        p2 = calc(op2, p1, n3)
        print(p2, end="")
except:
    print("erro", end="")