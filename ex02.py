def soma_lista_aninhada(lista):
    return sum(soma_lista_aninhada(item) if isinstance(item, list) else item for item in lista)

# Solicita ao usuário que insira a lista
entrada = input("Digite a lista para somar (ex: [1, [2, 3], [4, [5, 6]], 7]): ")
lista_exemplo = eval(entrada)
print(soma_lista_aninhada(lista_exemplo))
