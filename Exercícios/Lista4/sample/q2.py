def calculaAreaRetangulo(lado1, lado2=0):
    if lado2 == 0:
        return lado1*lado1
    else:
        return lado1*lado2
print(calculaAreaRetangulo(2))
print(calculaAreaRetangulo(4,5))