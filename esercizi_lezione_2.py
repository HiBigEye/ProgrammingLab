#print 538 minutes in hours format
minutes = 538
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"Minutes: {minutes} = Hours: {hours}h {remaining_minutes}m")

print("\n\n")

#Ask to the user an integer and print its square and his cube
print("Scrivi un numero intero: ")
user_input = int(input())
print(f"Il numero inserito e': {user_input}")
print(f"Il quadrato e': {user_input ** 2}")
print(f"Il cubo e' {user_input ** 3}")

print("\n\n")

#Verify if an inserted number is even or odd
print("Inserisci un numero intero: ")
user_input = int(input())

if (user_input % 2 == 0):
    print(f"Il numero inserito e' pari")
else:
    print(f"Il numero inserito e' dispari")

#Define a function that takes as argumnet a word and a character and return how many times the character appears in the word
def count_character(word, char):
    count = 0
    for chars in word:
        if chars == char:
            count += 1
    return count

#Write a program that verify if a number inserted is prime
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

is_prime(user_input)


