import json

class Faturamento:

    faturamentos_diarios = {}

    def __init__(self, file_path):
        with open(file_path) as file:
            self.faturamentos_diarios = json.loads(file.read())

    def __str__(self):
        return str(self.faturamentos_diarios)

    def menor_valor_diario(self, mes, dia):

        if str(mes) in self.faturamentos_diarios:
            if (dia) in self.faturamentos_diarios[str(mes)]:
                return min(self.faturamentos_diarios[str(mes)][str(dia)])
        return 0
    
    def maior_valor_diario(self, mes, dia):    
        if str(mes) in self.faturamentos_diarios:
            if str(dia) in self.faturamentos_diarios[str(mes)]:    
                return max(self.faturamentos_diarios[str(mes)][str(dia)])
        return 0
    
    def valor_diario(self, mes, dia):
        if str(mes) in self.faturamentos_diarios:
            if str(dia) in self.faturamentos_diarios[str(mes)]: 
                return sum(self.faturamentos_diarios[str(mes)][str(dia)])
        return 0

    def media_mensal(self, mes):
        valor_mensal = 0
        for i in self.faturamentos_diarios[str(mes)]:
            valor_mensal += self.valor_diario(mes, i)

        return valor_mensal/len(self.faturamentos_diarios[str(mes)].keys())
    
    def valores_acima_da_media(self, mes):
        valores_acima_da_media = 0

        media = self.media_mensal(mes)

        for dia in self.faturamentos_diarios[str(mes)]:
            if self.valor_diario(mes, dia) > media:
                valores_acima_da_media += 1
        return valores_acima_da_media

    def relatorio(self):
        for mes in self.faturamentos_diarios:
            for dia in self.faturamentos_diarios:
                print("Menor valor diario " + str(dia) + "/" + str(mes) + ": " + str(self.menor_valor_diario(mes, dia)))
                print("Maior valor diario " + str(dia) + "/" + str(mes) + ": " + str(self.maior_valor_diario(mes, dia)))
            print("Valores acima da média do mês " + str(mes) + ": " + str(self.valores_acima_da_media(mes)))
    


faturamento = Faturamento("faturamento_diario_numerico.json")

faturamento.relatorio()


