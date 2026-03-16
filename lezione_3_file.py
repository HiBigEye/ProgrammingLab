my_file = open('shampo_sales.txt', 'r') #<-- se voglio scriverci userò 'w' anzichè 'r'
print(my_file.read()) #<-- leggo il contenuto sottoforma di read
my_file.close()

my_file_1 = open('shampo_sales.txt', 'r')
print(my_file_1.read()[0:50]) #<-- Uso lo slicing per aprire solo parte del file
my_file_1.close()

my_file_1 = open('shampo_sales.txt', 'r')
print(my_file.readline())
print(my_file.readline())#<-- leggo riga per riga
print(my_file.readline())
my_file.close()

my_file_1 = open('shampo_sales.txt', 'r')
for line in my_file:
    print(line)
my_file.close()

with open('shampoo_sales.csv') as file:  #<-- così non serve chiudere il file
    print(file.read())

with open('shampoo_sales.csv') as file:
    print(file.readline())




