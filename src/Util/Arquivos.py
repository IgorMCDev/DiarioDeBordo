import os
import pandas

class Arquivo():
    def __init__(self, path):
        self.path_arquivo = os.path.normpath(path)
        self.nome_arquivo = os.path.basename(self.path_arquivo)
        self.local_arquivo = os.path.dirname(self.path_arquivo)

    def _existe_arquivo(self):
        return os.path.isfile(self.path_arquivo)

class ArquivoCSV(Arquivo):
    def __init__(self, path, separador=';'):
        self.separador = separador
        super().__init__('{}{}'.format(path, '.csv') if '.csv' not in path else path)
        
    def _ler_arquivo_csv_df(self):
        return pandas.read_csv(self.path_arquivo, sep=self.separador)
    
    def _gera_arquivo_csv(self, df_arquivo):
        return df_arquivo.to_csv(os.path.join(self.local_arquivo, self.nome_arquivo), index=False, sep=self.separador)