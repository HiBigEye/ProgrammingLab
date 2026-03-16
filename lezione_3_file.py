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

import os
cwd = os.getcwd()
#cwd <-- vedo la cartella corrente in cui mi trovo

os.path.abspath('shampoo_sales.csv') #<-- restituisce il path assoluto del file

mia_stringa = 'Date,Sales\n' #<-- simulazione della riga di intestazione del file
lista_elementi = mia_stringa.split(',') #<-- uso split con ',' come separatore per avere 2 elementi separati in un array
print(lista_elementi)

mia_stringa_2 = '5.5' #<-- il dato estratto dal csv è in formato string, noi lo vogliamo numerico
mio_numero = float(mia_stringa_2) #<-- usiamo il cast!

mia_lista = [1,2,3] #<-- supponiamo di aver estratto 3 dati e di volerne aggiungere 1 nuovo
mia_lista.append(4) #<-- in questo modo aggiungo un nuovo dato

####################################################################
#ESEMPIO COMPLETO#
####################################################################

values = [] #Inizializzo una lista vuota per salvare i valori

my_file = open('shampoo_sales.csv', 'r') #apro e leggo il file

for line in my_file: #leggo il file linea per linea

    elements = line.split(',') #per ogni linea separo gli elementi delle due colonne

    if elements[0] != 'Date': #se NON sto processando l'intestazione

        date = elements[0] #assegno alla variabile 'date' il valore della prima colonna
        value = elements[1] #

        values.append(value) #aggiungo alla lista dei valori il valore della riga n-esima




