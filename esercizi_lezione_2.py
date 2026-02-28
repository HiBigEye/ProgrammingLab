#print 538 minutes in hours format
print("ESERCIZIO 1)\n")
minutes = 538
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"Minutes: {minutes} = Hours: {hours}h {remaining_minutes}m")

print("\n\n")

#Ask to the user an integer and print its square and his cube
print("ESERCIZIO 2)\n")
print("Scrivi un numero intero: ")
user_input = int(input())
print(f"Il numero inserito e': {user_input}")
print(f"Il quadrato e': {user_input ** 2}")
print(f"Il cubo e' {user_input ** 3}")

print("\n\n")

#Verify if an inserted number is even or odd
print("ESERCIZIO 3)\n")
print("Inserisci un numero intero: ")
user_input = int(input())

if (user_input % 2 == 0):
    print(f"Il numero inserito e' pari")
else:
    print(f"Il numero inserito e' dispari")

print("\n\n")

#Define a function that takes as argumnet a word and a character and return how many times the character appears in the word
print("ESERCIZIO 4)\n")
def count_character(word, char):
    count = 0
    for chars in word:
        if chars == char:
            count += 1
    return count

print("Inserisci una parola: ")
word = str(input())
print("Inserisci una lettera: ")
char = str(input())

print(count_character(word, char))
print("\n\n")


#Write a program that verify if a number inserted is prime
print("ESERCIZIO 5)\n")
print("Enter a number to check if is prime")
user_input = int(input())

def is_prime(number):
    if number <= 3:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True

print(is_prime(user_input))

print("\n\n")

#write a program that sum n numbers inserted by the user
print("ESERCIZIO 6)\n")
def sum_numbers():
    print("Questo programma somma i numeri che inserisci.\nInserisci n numeri a piacere o 0 per uscire: ")
    number = int(input())
    sum = 0
    while (number != 0):
        sum += number
        number = int(input())
    print(f"La somma dei numeri inseriti e': {sum}")
    return

sum_numbers()

print("\n\n")

#write a program that compute the factorial through an iterative function
print("ESERCIZIO 7)\n")
def factorial():
    print("Inserisci il numero per cui calcolare il fattoriale: ")
    user_input = int(input())
    factorial = 1
    if user_input <= 1:
        return 1
    else:
        i = user_input
        while i != 1:
            factorial *= i
            i -= 1
    return factorial

print(factorial())

print("\n\n")

#scrivi un programma che dice all'utente se 3 numeri inseriti possono essere i lati di un triangolo ed eventualmente di quale tipo
print("ESERCIZIO 8)\n")
def is_triangle():
    print("Inserisci la misura del primo lato:")
    lato_1 = int(input())
    print("Inserisci la misura del secondo lato:")
    lato_2 = int(input())
    print("Inserisci la misura del terzo lato:")
    lato_3 = int(input())
    if lato_1+lato_2 > lato_3 or lato_1+lato_3 > lato_2 or lato_2+lato_3 > lato_1:
        print("I numeri inseriti possono essere i lati di un triangolo!\nControllo quale tipo di triangolo...")
        if lato_1==lato_2==lato_3:
            print("E' un triangolo equilatero!")
        elif (lato_1==lato_2 and lato_1 != lato_3) or (lato_1==lato_3 and lato_1 != lato_2) or (lato_2==lato_3 and lato_2 != lato_1):
            print("E' un triangolo isoscele!")
        else:
            print("E' un triangolo scaleno!")
    
    return

is_triangle()

print("\n\n")

#Scrivi un programma che conta quante vocali ci sono in una parola
print("ESERCIZIO 8)\n")
def vocals_counter(word):
    count = 0
    vocals = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in vocals:
            count+=1
    return count
print("Inserire una parola:")
word = str(input())
print(vocals_counter(word))
        




