class Atleta():
    def __init__ (self,peso):
        self.peso = peso
        self.aposentado = False
        self.aquecendo = False
        self.correndo = False
        self.nadando = False
        self.pedalando = False

    def aposentar(self):
        if self.aposentado == True:
            print (f'O atleta já está aposentado')
        else:
            print(f'O atleta está foi aposentado')
            self.aposentado = True
    def aquecer(self):
        if self.aquecendo == True:
            print(f'O atleta já está aquecendo')
        else:
            print(f'O atleta foi aquecer')
            self.aquecendo = True

class Corredor(Atleta):
    def __init__(self, peso):
        super(). __init__ (peso)

    def correr(self):
        if self.aquecendo == True:
            if self.aposentado == False:
                print(f'O Jogador está correndo')
            else:
                print(f"Está aposentado")
        else:
            print(f"Precisa aquecer")

class Nadador(Atleta):
    def __init__ (self,peso):
        super().__init__ (peso)

    def nadar(self):
        if self.aquecendo == True:
            if self.aposentado == False:
             print(f'O Jogador está nadando')
            else:
                print("O atleta está aposentado")
        else:
            print("O atleta precisa aquecer")
class Ciclista(Atleta):
    def __init__ (self,peso):
        super(). __init__ (peso)

    def pedalar(self):
        if self.aquecendo == True:
            if self.aposentado == False:
                print(f"O atleta está pedalando")
            else:
                print("está aposentado")
        else:
            print("Precisa aquecer")

c1 = Ciclista (50)

c1.pedalar()