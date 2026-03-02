my_file = open('shampo_sales.txt', 'r')
print(my_file.read()) #<-- leggo il contenuto sottoforma di read
my_file.close()

my_file_1 = open('shampo_sales.txt'), 'r')
print(my_file_1.read()[0:50]) #<-- Uso lo slicing per aprire solo parte del file
my_file_1.close()

