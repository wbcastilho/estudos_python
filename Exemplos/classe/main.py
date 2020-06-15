# Classes

class Computador:
    # Método Construtor da Classe
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print("Estou desligando")

    def Exibir(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

# Instância da classe computador
computador1 = Computador('Asus','8gb','Nvidia')
computador1.Exibir()