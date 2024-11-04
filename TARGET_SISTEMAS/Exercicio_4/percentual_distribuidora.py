import json

SP = "SP"
RJ = "RJ"
MG = "MG"
ES = "ES"
OUTROS = "Outros"

class Faturamento:

    faturamento_mensal = {}

    def __init__(self, file_path):
        with open(file_path) as file:
            self.faturamento_mensal = json.loads(file.read())

    def faturamento_mensal_por_estado(self, estado):
        return float(self.faturamento_mensal[estado])

    def total_faturamento(self):
        total_faturamento = 0
        for estado in self.faturamento_mensal:
            total_faturamento += self.faturamento_mensal_por_estado(estado)
        return total_faturamento
    
    def percentual_mensal(self, estado):
        return (100 * self.faturamento_mensal_por_estado(estado)) / self.total_faturamento()
    
    def relatorio(self):
        for estado in self.faturamento_mensal:
            print("Percentual mensal de " + estado + ": " + str(self.percentual_mensal(estado)))


faturamento = Faturamento("percentual_distribuidora.json")

faturamento.relatorio()