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

