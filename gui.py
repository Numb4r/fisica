# # (width, height) = (640, 480)


# import math

# def lei_de_snell(n1, n2, theta1_deg):
#     # Convertendo o ângulo de graus para radianos
#     theta1_rad = math.radians(theta1_deg)

#     # Calculando o ângulo de refração usando a Lei de Snell
#     theta2_rad = math.asin((n1 / n2) * math.sin(theta1_rad))

#     # Convertendo o ângulo de radianos de volta para graus
#     theta2_deg = math.degrees(theta2_rad)

#     return theta2_deg

# # Exemplo de uso
# n1 = 1.52  # Índice de refração do primeiro meio
# n2 = 1.0  # Índice de refração do segundo meio
# theta1 = 21  # Ângulo de incidência em graus

# theta2 = lei_de_snell(n1, n2, theta1)
# print(f"Ângulo de refração: {theta2:.2f} graus")
from tkinter import *
r=[]
class Application:
    def __init__(self, master=None):
        self.master = master
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados dos materiais")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # Entradas para o Material 1
        self.nomeLabel1 = Label(self.segundoContainer, text="Nome Material 1", font=self.fontePadrao)
        self.nomeLabel1.pack(side=LEFT)

        self.nomeMaterial1 = Entry(self.segundoContainer)
        self.nomeMaterial1["width"] = 30
        self.nomeMaterial1["font"] = self.fontePadrao
        self.nomeMaterial1.pack(side=LEFT)

        self.indiceLabel1 = Label(self.terceiroContainer, text="Índice de Refração Material 1", font=self.fontePadrao)
        self.indiceLabel1.pack(side=LEFT)

        self.indiceMaterial1 = Entry(self.terceiroContainer)
        self.indiceMaterial1["width"] = 30
        self.indiceMaterial1["font"] = self.fontePadrao
        self.indiceMaterial1.pack(side=LEFT)
         # Variável de controle para o campo de índice de refração

        # Entradas para o Material 2
        self.nomeLabel2 = Label(self.segundoContainer, text="Nome Material 2", font=self.fontePadrao)
        self.nomeLabel2.pack(side=LEFT)

        self.nomeMaterial2 = Entry(self.segundoContainer)
        self.nomeMaterial2["width"] = 30
        self.nomeMaterial2["font"] = self.fontePadrao
        self.nomeMaterial2.pack(side=LEFT)

        self.indiceLabel2 = Label(self.terceiroContainer, text="Índice de Refração Material 2", font=self.fontePadrao)
        self.indiceLabel2.pack(side=LEFT)

        self.indiceMaterial2 = Entry(self.terceiroContainer)
        self.indiceMaterial2["width"] = 30
        self.indiceMaterial2["font"] = self.fontePadrao
        self.indiceMaterial2.pack(side=LEFT)

        # Botão OK
        self.okButton = Button(self.quartoContainer)
        self.okButton["text"] = "OK"
        self.okButton["font"] = ("Calibri", "8")
        self.okButton["width"] = 12
        self.okButton["command"] = self.salvarInformacoes
        self.okButton.pack()
   
    def salvarInformacoes(self):
        self.material1 = {
            'nome': self.nomeMaterial1.get(),
            'indice_refracao': self.indiceMaterial1.get()
        }

        self.material2 = {
            'nome': self.nomeMaterial2.get(),
            'indice_refracao': self.indiceMaterial2.get()
        }
        r.append(self.material1)
        r.append(self.material2)
        # Salvar as informações em uma variável externa
        # Você pode usar as variáveis 'material1' e 'material2' conforme necessário
        self.master.destroy()


    
   
