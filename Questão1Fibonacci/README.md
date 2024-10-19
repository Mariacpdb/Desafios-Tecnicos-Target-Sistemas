# Código da primeira questão

Este código em Python  está dividido em diferentes partes, cada uma desempenhando um papel específico. 

## 1. Definição da função pertence_fibonacci(numero)

```python
def pertence_fibonacci(numero):
```

````def:```` Palavra-chave que define uma função em Python. Neste caso, estamos criando a função ````ertence_fibonacci.```` 

````numero:```` O parâmetro ````numero```` é o valor que será passado para a função, que será o número a ser verificado.

## 2. Inicialização das variáveis ````X```` e ````Y````

``` python
        X, Y = 0, 1
```
Aqui, as variáveis ````X```` e ````Y```` representam os primeiros dois números da sequência de Fibonacci.

````X```` começa como 0.

````Y```` começa como 1.

Esses valores são os primeiros dois números da sequência de Fibonacci.

 ## 3. Verificação dos casos especiais

```python
    if numero == 0 or numero == 1:
        return True

```

```if numero == 0 or numero == 1:```: Esta condição verifica se o número é 0 ou 1. Como ambos os números são os primeiros números da sequência de Fibonacci, se o número inserido for 0 ou 1, a função retorna ```True```.

```return True```: A função retorna o valor ```True```, indicando que o número pertence à sequência de Fibonacci.
      
## 4. Laço while para calcular a sequência de Fibonacci

````python
        while Y <= numero:
````
````while````: Um laço while que continua executando enquanto o valor de ````Y```` for menor ou igual ao número fornecido. O objetivo aqui é gerar os números da sequência de Fibonacci até que ````Y```` seja maior ou igual ao número fornecido.

## 5. Verificação dentro do laço while

````python
        if Y == numero:
            return True
````

````if Y == numero:````: Dentro do laço, a função verifica se o valor de ````Y```` é igual ao número fornecido. Se for, significa que o número fornecido pertence à sequência de Fibonacci, e a função retorna ````True````.

## 6. Atualização dos valores de ````X```` e ````Y```` para gerar a sequência

````python
        X, Y = Y, X + Y
````
Aqui, a função ````verificacao_a```` é chamada e o valor da variável ````texto```` (a string que o usuário digitou) é passado como argumento para a função.

Aqui está a lógica para gerar a sequência de Fibonacci:

O valor de ````X```` recebe o valor de ````Y````.

O valor de ````Y```` é atualizado para a soma dos valores anteriores de ````X```` e ````Y````. Isso faz com que ````X```` e ````Y```` avancem na sequência de Fibonacci.

## 7. Retorno caso o número não esteja na sequência

````python
    return False
````
Se o laço ````while```` terminar e nenhum valor de ````Y```` for igual ao número fornecido, a função retorna ````False````, indicando que o número não pertence à sequência de Fibonacci.`

## 8. Entrada do número pelo usuário

````python
numero_fibonacci = int(input("Digite um número para verificar se ele pertence à sequência Fibonacci: "))
````
````input()````: Solicita que o usuário insira um número.


````int()````: Converte a string fornecida pelo input() em um número inteiro.

````numero_fibonacci````: A variável que armazena o número digitado pelo usuário.

## 9. Chamada da função ````pertence_fibonacci```` e verificação

````python
if pertence_fibonacci(numero_fibonacci):
    print(f"O número {numero_fibonacci} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_fibonacci} não pertence à sequência de Fibonacci.")
````


````if pertence_fibonacci(numero_fibonacci):````: Chama a função ````pertence_fibonacci```` com o número fornecido pelo usuário e verifica se o retorno é ````True```` ou ````False````.

````print()````: Dependendo do resultado da função, imprime se o número pertence ou não à sequência de Fibonacci.