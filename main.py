def ser_primo(número):
    if número <= 1:
        return False
    for i in range(2, número):
        if número % i == 0:
            return False
    return True
n = int(input("Digite um número inteiro: "))
primos = [número for número in range(2, 10000) if ser_primo(número)]
for i in range(n):
    print(primos[i])