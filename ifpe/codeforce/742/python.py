input_valor = int(input())
if input_valor == 0:
    resultado = 1
else:
    input_valor = input_valor % 4
    if input_valor == 1:
        resultado = 8 
    if input_valor == 2:
        resultado = 4
    if input_valor == 3:
        resultado = 2
    if input_valor == 0:
        resultado = 6

print(resultado)
