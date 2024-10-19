def pertence_fibonacci(numero):
   
    X, Y = 0, 1

    
    if numero == 0 or numero == 1:
        return True
    
    while Y <= numero:
        if Y == numero:
            return True
        X, Y = Y, X + Y
    return False

numero_fibonacci = int(input("Digite um número para verificar se ele pertence a sequência Fibonacci: "))


if pertence_fibonacci(numero_fibonacci):
    print(f"O número {numero_fibonacci} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_fibonacci} não pertence à sequência de Fibonacci.")