import time
from input import lerArquivo
from lexicalScanner import tokenizador
codigo=lerArquivo("code.txt")
start_time = time.time()
tokenizador(codigo)
end_time = time.time()
execution_time = end_time - start_time
print(f'Tempo de execução: {execution_time} segundos')
print('done')