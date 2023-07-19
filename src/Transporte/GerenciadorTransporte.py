import os
import pandas
from src.Util.Mensagens import Mensagens
from src.Tabelas.InfoCorridasDia import INFO_CORRIDAS_DIA
from src.Util.Arquivos import ArquivoCSV

class GerenciadorTransporte():
    def __init__(self):
        self.mensagem = Mensagens()
        self.arquivo_transporte = None
   
    def __cria_linha_info_corrida(self, data, df_info_transporte):
        nova_linha = None
        try:
            df_filter_data = df_info_transporte[df_info_transporte['DATA_INICIO'] == data]
            dt_refe = data.strftime('%Y-%m-%d')
            qt_corr = len(df_filter_data)
            qt_corr_neg = len(df_filter_data[df_filter_data['CATEGORIA'].str.contains('Negocio')])
            qt_corr_pess = len(df_filter_data[df_filter_data['CATEGORIA'].str.contains('Pessoal')])
            vl_max_dist = float(df_filter_data['DISTANCIA'].max())
            vl_min_dist = float(df_filter_data['DISTANCIA'].min())
            vl_avg_dist = df_filter_data['DISTANCIA'].mean()
            qt_corr_reuni = len(df_filter_data.loc[(df_filter_data['PROPOSITO'].isnull() != True) & 
                                                   (df_filter_data['PROPOSITO'].str.contains('Reunião') == True)])
            qt_corr_nao_reuni = len(df_filter_data.loc[(df_filter_data['PROPOSITO'].isnull() != True) & 
                                                       (df_filter_data['PROPOSITO'].str.contains('Reunião') == False)])
            nova_linha = {'DT_REFE': dt_refe, 
                          'QT_CORR': qt_corr, 
                          'QT_CORR_NEG': qt_corr_neg, 
                          'QT_CORR_PESS': qt_corr_pess, 
                          'VL_MAX_DIST': vl_max_dist, 
                          'VL_MIN_DIST': vl_min_dist, 
                          'VL_AVG_DIST': vl_avg_dist, 
                          'QT_CORR_REUNI': qt_corr_reuni, 
                          'QT_CORR_NAO_REUNI': qt_corr_nao_reuni}
        except Exception as e:
            print('Erro ao criar linha. Erro: {}'.format(str(e)))
        return nova_linha

    def __processa_corridas_diarias(self, df_info_transporte):
        try:
            info_corridas_dia = INFO_CORRIDAS_DIA
            df_info_transporte["DATA_INICIO"] = pandas.to_datetime(df_info_transporte["DATA_INICIO"])
            df_info_transporte["DATA_INICIO"] = [data.date() for data in df_info_transporte["DATA_INICIO"]]
            datas = df_info_transporte["DATA_INICIO"].unique()
            for data in datas:
                nova_linha = self.__cria_linha_info_corrida(data, df_info_transporte)
                if nova_linha:
                    info_corridas_dia = pandas.concat([info_corridas_dia, pandas.DataFrame([nova_linha])], ignore_index=True)
            return info_corridas_dia
        except Exception as e:
            print('Erro ao contabilizar os dados do arquivo. Erro: {}'.format(str(e)))

    def __obtem_informacoes_usuario(self):
        tentativas = 0
        while tentativas < 3:
            try:
                self.mensagem._enviaMensagem(self.mensagem.CONST_ARQUIVO) 
                resposta_arquivo_pasta = self.mensagem._aguardaEscolha()
                if (resposta_arquivo_pasta == 'Y') or (resposta_arquivo_pasta == 'y'):
                    nome_arquivo_transporte = 'info_transportes'
                    path_arquivo_transporte = os.getcwd()
                    self.arquivo_transporte = ArquivoCSV(os.path.join(path_arquivo_transporte, nome_arquivo_transporte))
                elif (resposta_arquivo_pasta == 'N') or (resposta_arquivo_pasta == 'n'):
                    self.mensagem._enviaMensagem(self.mensagem.CONST_INICIO_DIARIO) 
                    path_arquivo_transporte = self.mensagem._aguardaEscolha()
                    self.mensagem._enviaMensagem(self.mensagem.CONST_NOME_ARQUIVO) 
                    nome_arquivo_transporte = self.mensagem._aguardaEscolha()
                    self.arquivo_transporte = ArquivoCSV(os.path.join(path_arquivo_transporte, nome_arquivo_transporte))
                else:	
                    self.mensagem._enviaMensagem(self.mensagem.YES_NO_QUESTION)
            except Exception as e:
                print('Erro ao obter as informações do usuário. Erro: {}'.format(str(e)))
            finally:
                if self.arquivo_transporte is not None:
                    break
                else:
                    tentativas += 1
                    if tentativas == 3:
                        self.mensagem._enviaMensagem(self.mensagem.ENCERRANDO_PROGRAMA)
    
    def _gera_info_corridas_diarias(self):
        try:
            self.__obtem_informacoes_usuario()
            if self.arquivo_transporte is not None:
                if self.arquivo_transporte._existe_arquivo():
                    df_info_transporte = self.arquivo_transporte._ler_arquivo_csv_df()
                    info_corridas_dia = self.__processa_corridas_diarias(df_info_transporte)
                    arquivo_corridas_diarias = ArquivoCSV(os.path.join(self.arquivo_transporte.local_arquivo, 'info_corridas_do_dia'))
                    arquivo_corridas_diarias._gera_arquivo_csv(info_corridas_dia)
                    print('Arquivo "info_corridas_do_dia" gerado com sucesso.')
                else:
                    print('O arquivo {} não existe. Verificar se o arquivo realmente existe no local indicado.'.format(
                        self.arquivo_transporte.path_arquivo))
        except Exception as e:
            print('Erro ao processar os dados para a corrida diária. Erro: {}'.format(str(e)))
