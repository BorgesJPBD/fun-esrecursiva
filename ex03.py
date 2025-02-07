def contar_caracteres(s, c):
    if not s:
        return 0
    return (s[0] == c) + contar_caracteres(s[1:], c)

s = input("Digite uma palavra: ")
c = input("Digite o caractere a ser contado: ")

print(contar_caracteres(s, c))