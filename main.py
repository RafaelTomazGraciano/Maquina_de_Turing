import json

def main():
    try:
        # Tenta abrir o arquivo JSON 
        with open("arquivo.json", "r") as arquivo_json:
            # Carrega os dados do arquivo JSON
            dados_json = json.load(arquivo_json)
    except FileNotFoundError:
        print("Erro: O arquivo 'arquivo.json' não foi encontrado.")
        return

    try:
        # Tenta abrir o arquivo txt
        with open("entrada1.txt", "r") as arquivo_txt:
            entrada = arquivo_txt.readlines()  # Le a fita e remove espaços extras
    except FileNotFoundError:
        print("Erro: O arquivo 'entrada.txt' não foi encontrado.")
        return
    
    transicoes = dados_json['transitions']  # Transições da máquina
    transicoes_dict = {(t['from'], t['read']): t for t in transicoes} # dicionário de transições para busca rápida
    simbolo_branco = dados_json['white']  # Simbolo que representa espaço em branco
    estados_finais = dados_json['final']  # Estados finais

    with open("saida.txt", "w") as arquivo_saida:
        for linha in entrada:
            
            fita = list(linha.strip())
            estado_atual = dados_json['initial']  # Estado inicial
            posicao_cabecote = 0  # Posição inicial do cabeçote
            
            # execução da maquina de turing
            while estado_atual not in estados_finais:
        
                chave_transicao = (estado_atual, fita[posicao_cabecote])
                # Procura pela transição correspondente
                if chave_transicao in transicoes_dict:
                    transicao = transicoes_dict[chave_transicao]
                    fita[posicao_cabecote] = transicao['write']
                    estado_atual = transicao['to']
                    posicao_cabecote += int(transicao['dir'])
                else:
                    break  # Não encontrou transição, então para a execução
        
                # Expande a fita se o cabeçote sair dos limites
                if posicao_cabecote < 0:
                    fita.insert(0, simbolo_branco)
                    posicao_cabecote = 0
                elif posicao_cabecote >= len(fita):
                    fita.append(simbolo_branco)

            # Escreve a fita final em um arquivo de texto
            arquivo_saida.write(''.join(fita) + '\n') 
    
            # Verifica se o estado final é de aceitação ou rejeição
            if estado_atual in estados_finais:
                print(1)  # Aceita
            else:
                print(0)  # Rejeita

if __name__ == "__main__":
    main()
