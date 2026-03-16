""""
LEZIONE SULLA PROGRAMMAZIONE AD OGGETTI

Prendiamo come esempio una lampadina: 
- cosa si può fare (accendere/spegnere) <-- AZIONI = METODI
- stato interno (acceso/spento) <-- STATO = CARATTERISTICHE

Possiamo definire queste due caratteristiche come un "template" della lampadina.

Due istanze (diverse lampadine) possono avere diverso STATO ma possiamo svolgere le stesse AZIONI su di loro
__________________________________________________________________________________________________
#Programmare ad oggetti vuol dire strutturare un programma aggregando oggetti, in cui ogni oggetto
#ha un tipo di comportamento e delle proprietà o stati dell'oggetto stesso.
__________________________________________________________________________________________________

Dato una determinata CLASSE DI OGGETTI, ad esempio un auto, posso definire diverse ISTANZE

Ad esempio con un auto posso definire il modello dell'auto (Nissan, Audi, Volvo ecc..) ciascuna delle quali
avrà delle proprietà peculiari

Per creare una istanza bisognerà specificare le caratteristiche di quella istanza

Ad esempio per la classe cane possiamo definire le caratteristiche razza, grandezza, età ecc.
Possiamo inoltre definire una serie di azioni che i cani possono compiere, ad esempio mangiare(), dormire() ecc.

L'ISTANZA di una CLASSE specifica quali sono gli attributi di quella specifica istanza

Su ognuna di quste istanze potrò applicare i metodi di quella classe
"""





"""
La OPP permette di ragionare in termini di entità e non solo di funzioni

Gli oggetti sono definiti con le classi

Una classe è uno schema che permette di descrivere un'entità con le caratteristiche desiderate

Negli oggetti/classi:
    funzioni si chiamano Metodi
    variabili si chiamano Attributi

Una volta inizializzati gli oggetti diventano ISTANZE -> si parla di istanziare una classe


Gli oggetti permettono di rappresentare bene le gerarchie (e caratteristiche comuni) e una volta istanziati
di mantenere facilmente lo stato (senza strutture di appoggio)
"""


"""
In Python le classi sono un modo di definire strutture dati (e operazioni su di esse)

La classe fornisce la struttura per qualcosa che deve essere definito senza però definire il contenuto

Sarà l'utente a scrivere i contenuti di ciascuna istanza della classe

IN PYTHON TUTTO è UN OGGETTO (la funzione dir() ritorna la lista di attributi e metodi di un oggetto)
"""


"""
è importante differenziare i metodi che ritornano qualcosa e i metodi(funzioni) in-place che modificano
l'oggetto ma non torna nulla!
Ad esempio print(my_list.reverse()) ritorna None mentre print(my_string.split()) ritorna una lista
"""

class NomeClasse: #<-- questo definisce una classe!
    pass #<-- classe vuota che non ha funzioni e attributi (ma che è definita!!)

classe = NomeClasse() #<-- istanzia una classe di oggetto (creo un oggetto specifico)
print(classe) #<-- posso stampare il contenuto di una classe (in questo caso è vuota)

"""
Abbiamo definito una classe ma non abbiamo definito metodi e attributi
"""

#ATTRIBUTI <-- impostati tramite il metodo __init(self,...)__ <-- chiamato costruttore

"""
Il metodo __init__ ha come argomenti:
    -self , che indica l'oggetto stesso (puntatore che punta su se stesso)
    - gli argomenti dopo il primo possono essere aggiunti per inizializzare lo stato dell'oggetto (altri attributi)
"""

print('----------------------------------------')

class Person():

    def __init__(self, name, surname): #<-- definisco gli attributi nell'ordine desiderato
        self.name = name #<-- attribuisco un nome agli attributi
        self.surname = surname 

person = Person('Mario', 'Rossi')
print(person)
print(person.name)
print(person.surname)

"""
Possiamo stabilire un attributo che sia comune a tutte le istanze
"""
print('------------------------')
class PersonNew():
    nazione = 'Italia'
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

new_person = PersonNew('Luca', 'Bianchi')
print(new_person.nazione)

"""
Si possono modificare gli attributi che abbiamo definito per una istanza specifica
"""
print('------------------------')

print(new_person.surname)

new_person.surname = 'Verdi'

print(new_person.surname)


"""
Si possono modificare anche gli attributi dell'intera classe MA NON è BUONA PRASSI!!!!
"""


#METODI <-- 










