# Código da segunda questão

Este código em Python faz a verificação da letra "a" (seja maiúscula ou minúscula) em uma string e conta quantas vezes ela aparece. 

## 1. Definição da função verificacao_a(string)

```python
def verificacao_a(string):
```
Aqui você está definindo uma função chamada verificacao_a. Esta função vai receber um parâmetro chamado string, que será a entrada do usuário.

## 2. Convertendo a string para minúsculas

``` python
    string_lower = string.lower()
```
A função ``` lower() ``` converte todos os caracteres da string em letras minúsculas. Isso é feito para que tanto "A" maiúscula quanto "a" minúscula sejam tratadas da mesma forma, simplificando a contagem.

Por exemplo, se o usuário inserir ``` "AbraCadabra" ``` essa string será convertida para ``` "abracadabra" ```

 ## 3. Contando quantas vezes a letra "a" aparece

      contagem = string_lower.count('a')
O método ````count('a') ````  conta quantas vezes a letra "a" (minúscula) aparece na string. Como toda a string foi convertida para minúsculas, qualquer ocorrência de "A" ou "a" será contada.
## 4. Verificação da contagem
````python
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")
````

```` if contagem > 0:```` Esta condição verifica se o número de vezes que a letra "a" aparece é maior que zero. Se for, isso significa que a letra "a" está presente na string.

Se a letra for encontrada, o código imprime a mensagem:

```` "A letra 'a' aparece {contagem} vezes na string."````, onde ````{contagem}```` é o número real de vezes que "a" aparece.

Se a letra "a" não for encontrada (ou seja, se ````contagem```` for igual a 0), o código imprime a mensagem ````"A letra 'a' não foi encontrada na string."````

## 5. Solicitando a entrada do usuário

````python
texto = input("Digite uma string: ")
````
O programa usa a função ````input()```` para solicitar ao usuário que insira uma string. O que for digitado será armazenado na variável ````texto.````

## 6. Chamando a função ````verificacao_a````

````python
verificacao_a(texto)
````
Aqui, a função ````verificacao_a```` é chamada e o valor da variável ````texto```` (a string que o usuário digitou) é passado como argumento para a função.