class Canguro:

    def __init__(self, contenuto_tasca = None):
        if contenuto_tasca is None:
            self.contenuto_tasca = []
        else:
            self.contenuto_tasca = contenuto_tasca


    def in_tasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)

    def __str__(self):
        return f'In tasca: di: {self.contenuto_tasca}'
    
can = Canguro()
guro = Canguro()

can.in_tasca(3)
can.in_tasca('Penna')
can.in_tasca(True)

print(can)
print(guro)

#ESERCIZIO 1)

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
    
class Auto(Veicolo):
    def __init__(self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte
        self.speed = 0

    def __str__(self):
        super().__str__()
        return 'Auto "Modello: {} Marca: {} Anno: {} Velocità: {} Numero porte: {}"'.format(self.modello, self.marca, self.anno, self.speed, self.numero_porte)

ciao = Auto('Juke', 'Nissan', 2012, 5)
print(ciao)
ciao.accelerare()
ciao.accelerare()
print(ciao)


###############################################################################################################
#ESERCIZIO 2)
###############################################################################################################

class Persona():
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
    
    def saluta(self):
        print('Ciao sono', self.ruolo + ',', self.nome, self.cognome)

class Studente(Persona):

    def __init__(self, ruolo, nome, cognome, corso = None):
        super().__init__("Studente UNITS", nome, cognome)
        self.corso = []

    def aggiungi_corso(self, materia):
        self.corso.append(materia)

    def saluta(self):
        Persona.saluta(self)
        print("Corsi = ", self.corso)
        

class Docente(Persona):

    def __init__(self, ruolo, nome, cognome, corso):
        super().__init__('Docente UNITS', nome, cognome)
        self.corso = []

    def saluta(self):
        Persona.saluta(self)
        print('Sono un docente dei corsi: ', self.corso)
    
    def aggiungi_corso(self, materia):
        self.corso.append(materia)

yuri = Studente('Studente','Yuri', 'Occhiogrosso','AIDA')

yuri.saluta()

nenzi = Docente('Docente UNITS', 'Laura', 'Nenzi', 'Laboratorio di Programmazione')

nenzi.saluta()

yuri.aggiungi_corso("Analisi 1")
yuri.aggiungi_corso("Algebra Lineare")

yuri.saluta()

nenzi.aggiungi_corso('Laboratorio di Programmazione')
nenzi.aggiungi_corso('Biologia computazionale')

nenzi.saluta()

###############################################################################################################
#ESERCIZIO 3)
###############################################################################################################

class Persona():
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
    
    def saluta(self):
        print('Ciao sono', self.ruolo + ',', self.nome, self.cognome)

class Studente(Persona):

    def __init__(self, ruolo, nome, cognome, corso = None):
        super().__init__("Studente UNITS", nome, cognome)
        self.corso = []

    def aggiungi_corso(self, materia):
        self.corso.append(materia)

    def saluta(self):
        Persona.saluta(self)
        print("Corsi = ", self.corso)

        

class Docente(Persona):

    def __init__(self, ruolo, nome, cognome, corso):
        super().__init__('Docente UNITS', nome, cognome)
        self.corso = []

    def saluta(self):
        Persona.saluta(self)
        print('Sono un docente dei corsi: ', self.corso)
    
    def aggiungi_corso(self, materia):
        self.corso.append(materia)

    def corsi_comuni(self, studente):
        check = True
        for corsi in studente.corso:
            if corsi not in self.corso:
                check = False
                break
        if check:
            print("L'insegnante copre tutti i corsi dello studente!")
            return True
        else:
            print("L'insegnante non copre tutti i corsi dello studente!")
            return False