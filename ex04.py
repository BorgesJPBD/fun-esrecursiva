def indice_maior_elemento(lista, indice=0, maior_indice=0):
    
    if indice == len(lista):
        return maior_indice
    
   
    if lista[indice] > lista[maior_indice]:
        maior_indice = indice
    
    return indice_maior_elemento(lista, indice + 1, maior_indice)

entrada = input("Digite os números separados por espaço: ")
lista = list(map(int, entrada.split()))


indice = indice_maior_elemento(lista)


print(f"Saída Esperada:\n{indice} # O maior elemento é {lista[indice]}, que está no índice {indice}")
