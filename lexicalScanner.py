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
                if char in (" ", ";", "<", ">", "=", "-", "+"):
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
                            tokenAtual = ""
                    elif char != " ":
                        escritor.writerow([char,tipo,len(tokenAtual),(l, i)])
                else:
                    tokenAtual += char
                i += 1
            if tokenAtual:
                if verificaToken(tokenAtual):
                    escritor.writerow([tokenAtual,tipo,len(tokenAtual),(l, i)])
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
    tokens = {
        "reservadas": ("while", "do"),
        "operadores": ("<", "=", "+"),
        "terminador": (";"),
        "identificador": ("i", "j")
    }
    if is_number(token):
        if len(token) > 1:
            return "constante"
        else:
            return "numero"
    for tipo, valores in tokens.items():
        if token in valores:
            return tipo
    return None


