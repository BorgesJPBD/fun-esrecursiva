revertida = input("Digite uma palavra para reverter: ")

def reverter_caracteres(s):
    if s == "":
        return s
    return s[-1] + reverter_caracteres(s[:-1])

print(reverter_caracteres(revertida))