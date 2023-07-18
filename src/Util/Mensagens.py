class Mensagens():
    def __init__(self):
        self.CONST_INICIO_DIARIO =  'Defina um workspace para a análise:'
        self.CONST_NOME_ARQUIVO = 'Qual o nome do arquivo que possui as informações de transporte?'

    def _enviaMensagem(self, mensagem):
        print(mensagem)

    def _aguardaEscolha(self):
        return input()