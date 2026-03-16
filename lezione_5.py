##################################################################################################
################# LEZIONE 5: ACCESSO ED EREDITARIETÀ"#############################################
##################################################################################################

#Alcuni attributi e metodi potrebbero essere specifici dell'implementazione e vorremmo non renderli visibili
#Questo può essere interessante per non permettere l'accesso al codice per l'utente

#Ad esempio se usiamo una lista per implementare una coda vorremmo evitare che dall'esterno si acceda direttamente alla lista

#In generale i tipi di accesso si dividono in:
# PUBLIC : Accessibile a tutti
# PROTECTED : Accessibili alla classe stessa e alle sottoclassi
# PRIVATE : Accessibili solo dalla classe stessa

#L'utilizzo di metodi e attributi privati permette di cambiare implementazione senza dover cambiare chi usa la classe

#Python non supporta i modificatori public, protected e private. Si usano delle convenzioni:
# Pubblici : nessun cambiamento
# Protetti : inizia con "_" (esempio: _some_stuff)
# Privati : inizia con "__"

class Queue:

    def __init__(self):
        self._data = [] #<-- la lista è un attributo protetto non accessibile direttamente
    
    def enqueue(self, x):
        self._data.append(x)
    
    def dequeue(self):
        return self._data.pop(0)
    
