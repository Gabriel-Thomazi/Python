"""
Leia duas cadeias de caracteres A e B. Determine quantas vezes a cadeia A ocorre na
cadeia B.
"""

def conta_ocorrencia(A, B):
    return B.count(A)



A = str(input("Digite alguma coisa: "))
B = str(input("Digite outra coisa: "))

resultado = conta_ocorrencia(A, B)
print(f"A cadeia ocorre {resultado} vezes.")
