#Lezione 3 del corso LISTE E FILE

#In python le liste sono un tipo
mia_stringa = "ciao mondo"
mia_stringa[2] #terzo carattere della stringa
mia_stringa[-1] #Ultimo carattere della stringa

#SLICING DELLE STRINGHE
mia_stringa[0:50] #Dal primo al cinquantesimo carattere
mia_stringa[30:50] #Dal trentunesimo al cinquantesimo carattere
mia_stringa[0:-1] #Dal primo al penultimo carattere
mia_stringa[1:3:2] #Dal secondo al quarto carattere con intervallo di 2
mia_stringa[-1::-1] #Dall'ultimo carattere al primo con intervallo di -1

#I METODI DI UNA CLASSE
#Alcune funzioni sono specifiche della classe che stiamo utilizzando
#Se stiamo utilizzando una variabile stringa possiamo usare i metodi della classe stringa

#'mia_stringa'.nome_metodo()

#LISTE
#E' un tipo di dati, di elementi di qualsiasi tipo, anche diversi tra loro
my_list = [1,2,3] #Lista di interi
my_list = ['Marco', 'Irene', 'Paolo'] #Lista di stringhe
my_list = ['ciao', 2.0, 5, [10,20]] #Lista valida MA pericolosa!

#Per accedere agli elementi della lista si ragiona come per le stringhe
x = [1,2,3,5,7,45,66,23]
y = x[1:6:2] #dall'elemento di indice 1 all'elemento di indice 6(escluso), con step 2
z = x[::2] #dall'inizio alla fine con step 2
w = x[::] #intera lista

#come per le stringhe si possono fare operazione di concatenazione(+) e ripetizione(*)
print(['a', 'b'] + ['c', 'd', 'e']) #['a', 'b', 'c', 'd', 'e']
print(2*['a','b']) #['a', 'b', 'a', 'b']

#Metodi e liste
t = ['a', 'b']
t.append('c') #Equivalente della concatenazione (+)
print(t) #['a', 'b', 'c']

#La lista e' mutabile (A DIFFERENZA DELLE STRINGHE)
numeri = [42, 123]
numeri[1] = 5
print(numeri) #[42,5]

x = [1,2,3]
x[1:3] = [] #elimino gli elementi dall'indice 1 all'indice 3 escluso
print(x) #[1]

#Le stringhe non sono mutabili = sono immutabili
saluti = 'Hello World'
#saluti[2] = 'B' ------> %%expect TypeError

#Devo creare una nuova stringa necessariamente
nuova_stringa = 'B' + saluti[1:] #'B' concatenato con la porzione di lista dall'indice 1 alla fine ('B' sostituisce indice 0)
print(nuova_stringa) 

#OPERATORE DI APPARTENENZA
#""in""" e ""not in""" servono per vedere se un valore(elemento) è presente o non presente in una struttura di dati
#il tipo di dato in cui si verifica può essere di diverso tipo (stringa, lista, dizionario)
#viene utilizzato principalmente nei cicli for

lettere = ['a', 'b', 'c']
'a' in lettere #Ritorna True
for lettera in lettere:
    print(lettera) # a b c 

for i in range(len(lettere)):
    print(lettere[i])

for i, lettera in enumerate(lettere):
    print(i, lettera)

#Nel momento in cui si instanzia ad una nuova variabile una lista
#L'assegnazione rispetta la posizione in memoria della lista Quindi,
#A differenza delle stringhe, i metodi delle liste modificano l'oggetto di partenza
#per creare una copia della lista si possono utilizzare vari modi

lista_1 = [1,2,3]
lista_2 =  lista_1
lista_3 = lista_1[:]
lista_4 = lista_1.copy()

#E' fondamentale distinguere i metodi che modificano la lista di partenza e quelli che invece creano una nuova lista
#Ad esempio .append() non crea una nuova lista

lista_1 = [1,2,3]
lista_1.append(4)
print(lista_1) #[1,2,3,4]

#La differenza è importante quando bisogna scrivere funzioni che devono modificare la lista
#Ad esempio questa funziona non cancella il primo elemento
def non_decapita(t):
    t = t[1:] 

t_1 = [1,2,3,4]
non_decapita(t_1)
print(t_1)

#Non funziona perchè la variabile t è locale e non sta modificando la variabile globale passata per argomento

def decapita(t):
    return t[1:] 

decapita(t_1)
print(t_1)
#In questo caso funziona perché il valore di ritorno viene salvato nella variabile globale t_1 quando la funzione viene chiamata

#Una alternativa è quella di utilizzare nella funzione un metodo che modifica la lista di partenza



