texto = "while g   h for   -    i < 100 do  i = i +  j  ;\n"
repeticoes = 2

def gerar_entrada(texto, repeticoes):
    with open('code.txt', 'w') as file:
        for _ in range(repeticoes):
            file.write(texto)

def lerArquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        return [linha.rstrip('\n') for linha in file]
    
gerar_entrada(texto,repeticoes)
