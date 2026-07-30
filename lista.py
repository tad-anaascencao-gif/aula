def cria_lista():
    # variavel 'menores' vai para a Stack
    # a lista (1,2,3) vai para o Heap
    numeros = [1,2,3] 
    return numeros

resultado = cria_lista()
# A função acabou, mas a lista
# ainda existe no Heap
print(resultado) # [1,2,3]
