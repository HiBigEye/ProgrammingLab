#ESERCIZIO 1) Creazione classe veicolo, attributi e metodi

class Veicolo:

    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0

    def __str__(self):
        return 'Auto "Modello: {} Marca: {} Anno: {} Velocità: {}"'.format(self.modello, self.marca, self.anno, self.speed)
    
    def accelerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5
    
    def get_speed(self):
        return self.speed
    
audi = Veicolo('Punto', 'Fiat', 2006)
print(audi)

audi.accelerare()
print(audi)

audi.accelerare()
audi.accelerare()
audi.accelerare()
print(audi)

audi.frenare()
audi.frenare()
print(audi)

print(audi.get_speed())


#ESERCIZIO 2)

class CsvFile:

    def __init__(self, name):
        self.name = name

    def get_data(self):
        lista = []
        file = open(self.name, 'r')
        for line in file:
            elements = line.strip().split(',')
            lista.append(elements)
        file.close()
        return lista

file = CsvFile('shampoo_sales(in).csv')
print(file.get_data())

