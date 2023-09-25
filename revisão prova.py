
#Exercicio 1 !

def multiplo_cinco():
    numero_dado = int (input('Digite o numero:'))
    if numero_dado % 5 == 0:
        return True
    else:
        return False

# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário.
def multiplo_de_5():
    multiplo_5 = int(input("Digite um numero:"))
    if multiplo_5 % 5 == 0:
        return True
    elif multiplo_5 % 3 == 0:
        return True
    else:
        return False

# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.
def palavra_palin():
        nome = (input("Digite um palavra:"))
        if nome == nome [::-1]:
            return print("Essa palavra é palindromo.")
        else:
            return print("Essa palavra não é palindromo.")

    
# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja 
# comprar. O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de frutas que o usuário deseja comprar.
def lista_compras():
    lista = []
    while True: 
        fruta = (input("Digite as frutas, uma por uma:"))
        fruta_veia = fruta.lower()
        if fruta_veia == "sair":
            print (lista)
            exit()
        print("A fruta foi adicionada a lista.")
        lista.append(fruta_veia)


# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em metros
#  o programa retorna no console a área do círculo em m²
#  e o perímetro em metros.

def area_circulo():
    raio = float(input("Digite o raio de circulo em metros:"))
    pi = 3.1415
    area = pi * (raio * raio) 
    perimetro = 2 * pi * raio
    return print(f"O perimetro é: {perimetro:.2f}\nE a área é: {area:.2f}")


# Exercício 6: Faça um programa que solicita o ano de nascimento do usuário e retorna o seu signo no horóscopo chinês.

#### Dica: Para descobrir o seu signo no horóscopo chinês, você precisará conhecer o ano do seu nascimento de acordo com o calendário chinês. O horóscopo chinês é baseado em um ciclo de 12 anos, cada ano representado por um animal do zodíaco chinês. Aqui estão os 12 animais do zodíaco chinês e os anos correspondentes:

"""Rato: 2020, 2008, 1996, 1984, 1972, 1960, etc.
Boi (ou Búfalo): 2021, 2009, 1997, 1985, 1973, 1961, etc.
Tigre: 2010, 1998, 1986, 1974, 1962, 1950, etc.
Coelho (ou Gato): 2011, 1999, 1987, 1975, 1963, 1951, etc.
Dragão: 2012, 2000, 1988, 1976, 1964, 1952, etc.
Serpente: 2013, 2001, 1989, 1977, 1965, 1953, etc.
Cavalo: 2014, 2002, 1990, 1978, 1966, 1954, etc.
Cabra (ou Ovelha): 2015, 2003, 1991, 1979, 1967, 1955, etc.
Macaco: 2016, 2004, 1992, 1980, 1968, 1956, etc.
Galo (ou Galinha): 2017, 2005, 1993, 1981, 1969, 1957, etc.
Cão: 2018, 2006, 1994, 1982, 1970, 1958, etc.
Porco: 2019, 2007, 1995, 1983, 1971, 1959, etc.
"""

def signo_chines(ano):
    signo_chines = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cão", "Porco"]
    calculo = (ano - 1900) % 12
    return signo_chines[calculo]



# Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.

# Um número é primo quando é divisível apenas por 1 e por ele mesmo. Por exemplo, 2, 3, 5 e 7 são números primos, mas 4, 6, 8 e 9 não são.

def numero_primo(numero):
    if numero <= 1:
        return False
    elif numero <=3:
        return True
    else:
        for num in range(2, numero):
            if numero % num == 0:
                return False
            return True
    numero = int(input("Digite um número inteiro: ")) 



# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.

def email_vei(email):
    email_da_pessoa = input ("Digite seu email: ")
    if "@" in email:
        return True
    else:
        return False



# Exercício 9: Usando o método random(), crie um programa que solicita ao usuário que adivinhe um número inteiro entre 1 e 10 (contando o 10). Se o usuário digitar um número menor que 1 ou maior que 10, solicite que ele insira um número válido. Se o usuário digitar um número válido, verifique se o número que o usuário digitou é igual ao número gerado aleatoriamente pelo programa. Se o número for igual, imprima "Você acertou!". Caso contrário, imprima "Você errou!".

# Extra: Conte quantas tentativas o usuário precisou para acertar o número. Permita tentativas até o usuário acertar o número.

def jogo_de_advinhacao(numero):
    

    numero_de_tentativas = 1
    numero_sorteado = rd.randint(1, 11)
    while numero < 1 or numero > 10:
        print("Número inválido.")
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
    else:
        print("Número válido.")
    while numero != numero_sorteado:
        numero_de_tentativas += 1
        print("Você errou!")
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
    print(f"Você acertou! O número sorteado foi {numero_sorteado}. Você precisou de {numero_de_tentativas} tentativas para acertar o número.")
    
    

    numero = int(input("Digite um número inteiro entre 1 e 10: "))




    # Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.

def contador_de_a():
    frase = input('digite a frase: ')
    print("a volgal A aparece:", frase.count('a')+frase.count('A') ,"Vezes.")

print(contador_de_a())