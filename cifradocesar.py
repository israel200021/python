CLAVE = 26
def Menu():
    while (True):
        print('CIFRADO CESAR')
        print('¿Deseas encriptar o desencriptar un mensaje?')
        print('1.Encriptar')
        print('2.Desencriptar ')
        opcion = input('Selecciona una opcion: ').lower()
        if opcion == '1':
            return opcion
        elif opcion =='2':
            return opcion
        else:
            print('Ingresa una opcion correcta')
    

def texto(opcion):
    if opcion == '2':
        print('Ingrese el tecto que desaes desencriptar')
        return input()
    else:
        print('Ingresa el texto que desas encriptar :')
        return input()

def clave():
    clave = 0
    while True:
        print('Ingresa el número de clave (1-26)')
        clave = int(input())
        if (clave >= 1 and clave <= CLAVE):
            return clave

def traducido(opcion, mensaje, clave):

    if opcion == '2':
        clave= -clave
    traduccion = ''
    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave
            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
        elif num < ord('A'):
            num += 26
        elif simbolo.islower():
            if num > ord('z'):
                num -= 26
        elif num < ord('a'):
            num += 26
        traduccion += chr(num)
    else:
        traduccion += simbolo
    return traduccion

opcion = Menu()
mensaje = texto(opcion)
clave = clave()
print('Tu texto traducido es:')
print(traducido(opcion, mensaje, clave))
