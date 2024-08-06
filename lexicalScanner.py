import csv

def tokenizador(entrada):
    tokens = {}
    with open("tabelaTokens.csv", 'w', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow(['Token', 'Identificacao', 'Tamanho', 'Posicao']) 
        l = 0
        d=1
        while l < len(entrada):
            i = 0
            tokenAtual = ""
            linha = entrada[l]
            while i < len(linha):
                char = linha[i]
                if char in (" ", ";", "<", ">", "=", "+"):
                    tipo = verificaToken(tokenAtual)
                    if tokenAtual:
                        if tipo=="identificador" or tipo=="constante":
                            escritor.writerow([tokenAtual,tipo,len(tokenAtual),(l, i-1)])
                            if tokenAtual not in tokens:
                                tokens[tokenAtual]=d
                                d+=1
                            tokenAtual = "" 
                        elif tipo:
                            escritor.writerow([tokenAtual,tipo,len(tokenAtual),(l, i-1)])
                            tokenAtual = ""
                        else:
                            print(f"Token '{tokenAtual}' não identificado na posição {i} da linha {l}")
                            tokenAtual = ""
                    elif char != " ":
                        escritor.writerow([char,tipo,len(tokenAtual),(l, i)])
                else:
                    tokenAtual += char
                i += 1
            if tokenAtual:
                if verificaToken(tokenAtual):
                    escritor.writerow([tokenAtual,tipo,len(tokenAtual),(l, i)])
                else:
                    print(f"Token '{tokenAtual}' não identificado na posição {i} da linha {l}")
            l+=1
    with open("tabelaSimbolos.csv", 'w', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow(['Indice', 'Simbolo']) 
        for chave,valor in tokens.items():
            escritor.writerow([valor,chave])

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def verificaToken(token):
    tokens_dict = {
        "while": "reservada",
        "do": "reservada",
        "<": "operador",
        "=": "operador",
        "+": "operador",
        ";": "terminador",
        "i": "identificador",
        "j": "identificador"
    }
    tipo=tokens_dict.get(token, False)
    if tipo==False:
        if is_number(token):
            return "constante" if len(token) > 1 else "numero"

    return tipo

