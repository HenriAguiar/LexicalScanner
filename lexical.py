texto = "while     i < 100 do i =i + j;"

def tokenizador(entrada):
    tokens = {}
    tokenAtual = ""
    i = 0
    
    while i < len(entrada):
        char = entrada[i]
        
        if char in (" ", ";", "<", ">", "=", "-", "+"):
            if tokenAtual:
                tokens[i-1]=tokenAtual
                tokenAtual = ""
                
            if char != " ":
                tokens[i]=char
        else:
            tokenAtual += char
        
        i += 1
    
    if tokenAtual:
        tokens[i]=tokenAtual
    
    return tokens

def verificaToken(token):


print(tokenizador(texto))
print('done')