class Mensagens():
    def __init__(self):
        self.CONST_ARQUIVO = 'O arquivo de transportes encontra-se na pasta raiz do projeto? (Y/n)'
        self.YES_NO_QUESTION = 'É uma pergunta de sim ou não. Por favor, responda "Y" para sim ou "n" para não.'
        self.ENCERRANDO_PROGRAMA = 'Encerrando o programa por falta de informações.'
        self.CONST_INICIO_DIARIO =  'Defina um workspace para a análise (path): '
        self.CONST_NOME_ARQUIVO = 'Qual o nome do arquivo que possui as informações de transporte? (info_transportes)'

    def _enviaMensagem(self, mensagem):
        print(mensagem)

    def _aguardaEscolha(self):
        return input()