from pathlib import Path
from datetime import datetime
import os
import datetime as dt

# pasta alvo
path = Path(r'C:\Scan')

# coleta e separação de dia e mes atual
data_atual = datetime.now().strftime("%d %m %Y")
data_atual =  data_atual.split() 
dia_atual = data_atual[0]
mes_atual = data_atual[1]
ano_atual = data_atual[2]

# lista para os paths dos arquivos
paths = []

# def para verificar pasta alvo
def exist():
    if path.exists():
        tratamento()
        os.system('cls')
        print(f'Total de arquivos excluidos: {len(paths)}')
    else:
        print(f'Caminho Não Encontrado : "{path}" ')

def tratamento(): 
    # todos o arq da pasta alvo
    for i in Path(path).glob('*'):
        # pegar o tempo em segundos
        temp = os.path.getctime(i) 
        # separar o mes do arq
        mes_arq = dt.datetime.fromtimestamp(temp).strftime("%m")
        # separar o ano do arq
        ano_arq = dt.datetime.fromtimestamp(temp).strftime("%Y")
        
        if mes_arq != mes_atual or mes_arq != mes_atual and ano_arq != ano_atual or mes_arq == mes_atual and ano_arq != ano_atual :
            # separar o dia do arq
            dia_arq = dt.datetime.fromtimestamp(temp).strftime("%d")
            # data atual
            data_atual = datetime.strptime(f'{int(ano_atual)}-{int(mes_atual)}-{int(dia_atual)}', '%Y-%m-%d')
            # data arquivo
            data_arq = datetime.strptime(f'{int(ano_arq)}-{int(mes_arq)}-{int(dia_arq)}', '%Y-%m-%d')
            # soma em dias 
            quantidade_dias = abs((data_atual - data_arq).days)


            if not data_arq > data_atual:
                if quantidade_dias >= 30:
                    paths.append(i)

        try:
            for arquivo in paths:
                if arquivo.is_file():
                    arquivo.unlink()

        except(PermissionError,FileNotFoundError) as error:
            print(f'{error} no arquivo {arquivo}')
            

exist()     



