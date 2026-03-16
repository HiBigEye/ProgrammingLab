#1) Scrivere una funzione che sommi tutti gli elementi di una lista

print("ESERCIZIO 1) Scrivere una funzione che sommi tutti gli elementi di una lista")
def somma_elementi_lista(lista):
    somma = 0
    for i in lista:
        somma +=i
    
    return somma

lista = [1,2,3,4,5]
print(f"La somma degli elementi della lista è: {somma_elementi_lista(lista)}")

#Esercizio 2) Scrivi una funzione che prende in input una stringa e ritorna True se è un palindromo, False altrimenti
def is_palindrome(stringa):
    is_palindrome = 1
    for i in range(len(stringa)//2):
        if stringa[i]!=stringa[-i-1]:
            print(i, -i-1)
            is_palindrome = 0
        else:
            print(i, -i-1)
    
    if is_palindrome == 0:
        print("La stringa non è palindroma!")
        return False
    else:
        print("La stringa è palindroma!")
        return True
    
"""
versione più pulita

def is_palindrome(stringa):
    invert = stringa[::-1]      <-- Inverte la stringa da inizio a fine
    if(invert == stringa)
        return True
    return False
"""
        

stringa = "aabbaammaabbaa"
stringa_2 = "arcsjdofksjfkflc"
is_palindrome(stringa)
is_palindrome(stringa_2)

#Esercizio 3) Definire una funzione che prende in input una lista A, indici i,j, e scambia il valore di A[i] con A[j]
def scambia_valori(A, i, j):
    print(f"\nInverto la posizione {i} con la posizione {j}")
    temp = A[i]
    print("A[i]: ", A[i])
    A[i] = A[j]
    print("New A[i]:", A[i])
    print("A[j]", A[j])
    A[j] = temp
    print("New A[j]: ", A[j])
    return A

"""
Versione alternativa più pulita e pythonica

A = list(map(int, input("Inserire gli elementi della lista: ").split()))

i = int(input("Inserire il primo indice che si vuole scambiare: "))
j = int(input("Inserire il secondo indice che si vuole scambiare: "))

A[i], A[j] = A[j], A[i]

print(A)
"""

lista = [1,2,3,4,5]
print("\n\nLista Originale: ")
for i in lista:
    print(i)
scambia_valori(lista,0,4)
print("\nLista invertita: ")
for i in lista:
   print(i)

#4) Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno almeno un elemento in comune
def common_element(lista_1,lista_2):
    trovato = 0
    for i in lista_1:
        if i in lista_2:
            trovato = 1
    if trovato == 1:
        print("Elemento in comune trovato!")
        return True
    else:
        print("Nessun elemento in comune!")
        return False
    
"""
def common_elements(A,B):
    for elem in A:
        if elem in B:
            return True
    return False
"""
    
lista_1 = [1,3,5,6,4,2]
lista_2 = [33,2,88]

print(common_element(lista_1,lista_2))

lista_3 = [44,5,34]
lista_4 = [55,65,36,23]
print(common_element(lista_3,lista_4))

#Esercizio 5) Definire una funzione che prende in input una lista di numeri interi da 0 a 9 e restituisce
#gli stessi numeri in formato di stringa
def number_to_string(n):
    if n == 0: return "Zero"
    if n == 1: return "Uno"
    if n == 2: return "Due"
    if n == 3: return "Tre"
    if n == 4: return "Quattro"
    if n == 5: return "Cinque"
    if n == 6: return "Sei"
    if n == 7: return "Sette"
    if n == 8: return "Otto"
    if n == 9: return "Nove"
    else: return "Numero non ammesso"

def list_to_string(list):
    list_string = []
    for i in range(len(list)):
        x = list[i]
        list_string.append(number_to_string(x))
    return list_string

lista_base = [1,2,3,4,5,6,7,99]
lista_stringa = list_to_string(lista_base)

for i in lista_base:
    print(i)

for i in lista_stringa:
    print(i)
        

