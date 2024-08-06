import csv

texto = "while   g for  i < 100 do i =i + j;"

def tokenizador(entrada):
    tokens = {}
    tokenAtual = ""
    i = 0
    while i < len(entrada):
        char = entrada[i]
        if char in (" ", ";", "<", ">", "=", "-", "+"):
            tipo=verificaToken(tokenAtual)
            if tokenAtual:
                if tipo:
                    tokens[i-1]=tokenAtual
                    tokenAtual = ""
                else : 
                    print(f"Token '{tokenAtual}' não identificado na posição {i} da linha 0")
                    tokenAtual = ""
            elif char != " ":
                tokens[i]=char
        else:
            tokenAtual += char
        i += 1
    if tokenAtual:
        if verificaToken(tokenAtual):
            tokens[i]=tokenAtual
        else:
            print(f"Token '{tokenAtual}' não identificado na posição {i} da linha 0")
    return tokens

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def verificaToken(token):
    tokens={"reservadas":("while","do"),
            "operadores":("<","=","+"),
            "terminador":(";"),
            "identificador":("i","j")}
    for tipo,valores in tokens.items():
        if token in valores or is_number(token):
            return tipo
    return False


print(tokenizador(texto))
print('done')