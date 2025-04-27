def romano_a_decimal(romano):

    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }

    if romano == "":
        return 0

    primero = valores[romano[0]]
    if len(romano) > 1:
        segundo = valores[romano[1]]
    else:
        segundo = 0

    if primero < segundo:
        return (segundo - primero) + romano_a_decimal(romano[2:])

    return primero + romano_a_decimal(romano[1:])


entrada = input("Ingrese un número romano (I, V, X, L, C, D, M): ").upper()
resultado = romano_a_decimal(entrada)
print(f"{entrada} → {resultado}")
