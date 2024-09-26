def cifCesar(mens, desp):
    res = ""

    # Recorre cada letra del mensaje
    for i in mens:
        codascii = ord(i)  # Convierte la letra a código ASCII
        ncod = codascii + desp  # Aplica el desplazamiento

        # Asegura que la letra se mantenga dentro del alfabeto 'a-z'
        if codascii >= 97 and codascii <= 122:  # Minúsculas
            if ncod > 122:
                ncod -= 26  # Si se pasa de 'z', vuelve a 'a'
            elif ncod < 97:
                ncod += 26  # Si es antes de 'a', vuelve a 'z'
        
        # Convierte de vuelta el nuevo código ASCII a un carácter
        res += chr(ncod)

    return res  # Devuelve el mensaje cifrado o descifrado


# Uso del programa
mens = "hola mundo"
desp = 2

mens_cif = cifCesar(mens, desp)
print(mens_cif)