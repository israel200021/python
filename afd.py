# L(M) = { w en {a,b}* | w termina en b}
print ("\n# L(M) = { w en {a,b}* | w termina en b}\n")
Sigma = [ 'a' , 'b' ]
Q=['q0','q1']
s='q0'
F=['q1']
transiciones_delta = { ('q0','a') : 'q0', ('q0','b') : 'q1',
                       ('q1','a') : 'q0', ('q1','b') : 'q1'}
def delta( q , s ):
    global transiciones_delta
    return transiciones_delta[(q,s)]

L = [ 'b', 'ab', 'bbb', 'abababab', 'aaaaaaab']
UniversoMenosL = [ 'a', 'ba', 'bbbbba', 'aaaaaa', 'babababa','']

for w in L:
    estado=s
    for c in w:
        estado = delta( estado , c )
    if estado in F:
        print(w,"si esta en el lenguaje")
    else:
        print(w,"no esta en el lenguaje")

for w in UniversoMenosL:
    estado=s
    for c in w:
        estado = delta( estado , c )
    if estado in F:
        print(w,"si esta en el lenguaje")
    else:
        print(w,"no esta en el lenguaje")

# L = { w en {a,b,c}* | w no tiene la subcadena bc }
print ("\nL = { w en {a,b,c}* | w no tiene la subcadena bc }\n")
Sigma1 = [ 'a' , 'b', 'c' ]
Q1=['q0','q1','q2']
s1='q0'
F1=['q1','q0']
transiciones_delta1 = { ('q0','a') : 'q0', ('q0','b') : 'q1', ('q0','c') : 'q0',
        ('q1','a') : 'q0', ('q1','b') : 'q1', ('q1','c') : 'q2',
        ('q2','a') : 'q2', ('q2','b') : 'q2', ('q2','c') : 'q2'}
def delta1( q , s ):
    global transiciones_delta1
    return transiciones_delta1[(q,s)]

L1   = [ 'b', 'ab', 'bbb', 'abababab', 'aaaaaaab']
UniversoMenosL1 = [ 'abcb', 'bca', 'bbbbcba', 'aabcaaaa', 'babcababa','']

for w in L1:
    estado=s1
    for c in w:
        estado = delta1( estado , c )
    if estado in F1:
        print(w,"si esta en el lenguaje")
    else:
        print(w,"no esta en el lenguaje")

for w in UniversoMenosL1:
    estado=s1
    for c in w:
        estado = delta1( estado , c )
    if estado in F1:
        print(w,"si esta en el lenguaje") 
    else:
        print (w,"no esta en el lenguaje")


# L = { w en {0,1}* | w tiene un número impar de a's y un número par de b's }
print ("\nL = { w en {0,1}* | w tiene un número impar de a's y un número par de b's }\n")
Sigma2 = [ 'a' , 'b']
Q2=['q0','q1','q2','q3']
s2='q0'
F2=['q1']
transiciones_delta2 = { ('q0','a') : 'q1', ('q0','b') : 'q3',
        ('q1','a') : 'q0', ('q1','b') : 'q2', 
        ('q2','a') : 'q3', ('q2','b') : 'q1',
        ('q3','a') : 'q2', ('q3','b') : 'q0'}
def delta2( q , s ):
    global transiciones_delta2
    return transiciones_delta2[(q,s)]
L2 = [ 'abb', 'abaabbb', 'ababbba', 'aaa', 'aaaabaaab']
UniversoMenosL2 = [ '', 'ba', 'bbbbba', 'aabaaaa', 'ababbaba']

for w in L2:
    estado=s
    for c in w:
        estado = delta2( estado , c )
    if estado in F2:
        print(w,"si esta en el lenguaje")
    else:
        print(w,"no esta en el lenguaje")

for w in UniversoMenosL2:
    estado=s2
    for c in w:
        estado = delta2( estado , c )
    if estado in F2:
        print(w,"si esta en el lenguaje")
    else:
        print (w,"no esta en el lenguaje")

# L = { w en {a,b}* | el penúltimo símbolo de w es una a }
print ("\nL = { w en {a,b}* | el penúltimo símbolo de w es una a} \n")
Sigma3 = [ 'a' , 'b']
Q3=['q0','q1','q2','q3']
s3='q0'
F3=['q2','q3']
transiciones_delta3 = { ('q0','a') : 'q1', ('q0','b') : 'q0',
        ('q1','a') : 'q2', ('q1','b') : 'q3',
        ('q2','a') : 'q2', ('q2','b') : 'q3',
        ('q3','a') : 'q1', ('q3','b') : 'q0'}
def delta3( q , s ):
    global transiciones_delta3
    return transiciones_delta3[(q,s)]
L3 = [ 'ab', 'abaa', 'abbab', 'abababab', 'aaaaaaab']
UniversoMenosL3 = [ 'abb', 'ba', 'bbbbba', 'aabaaaba', 'babbaba','']

for w in L3:
    estado=s3
    for c in w:
        estado = delta3( estado , c )
    if estado in F3:
        print(w,"si esta en el lenguaje")
    else:
        print(w,"no esta en el lenguaje")

for w in UniversoMenosL3:
    estado=s3
    for c in w:
        estado = delta3( estado , c )
    if estado in F3:
        print(w,"si esta en el lenguaje")
    else:
        print (w,"no esta en el lenguaje")

# L = { w en {0,1}* | si w tiene la subcadena 11, debe ir precedida de la subcadena 00 }
print ("\nL = { w en {0,1}* | si w tiene la subcadena 11, debe ir precedida de la subcadena 00 }\n")
Sigma4 = [ '0' , '1']
Q4=['q0','q1','q2','q3','q4','q5','q6']
s4='q0'
F4=['q0','q1','q2','q3','q4','q5']
transiciones_delta4 = { ('q0','0') : 'q1', ('q0','1') : 'q5',
        ('q1','0') : 'q2', ('q1','1') : 'q5',
        ('q2','0') : 'q2', ('q2','1') : 'q3',
        ('q3','0') : 'q1', ('q3','1') : 'q4',
        ('q4','0') : 'q1', ('q4','1') : 'q6',
        ('q5','0') : 'q1', ('q5','1') : 'q6',
        ('q6','0') : 'q6', ('q6','1') : 'q6' }
def delta4( q , s ):
    global transiciones_delta4
    return transiciones_delta4[(q,s)]

L4 = [ '0011', '', '000', '00110011', '0100011']
UniversoMenosL4 = [ '011', '11', '010111', '0111', '1111','']

for w in L4:
    estado=s4
    for c in w:
        estado = delta4( estado , c )
    if estado in F4:
        print(w,"si esta en el lenguaje")
    else:
        print(w,"no esta en el lenguaje")

for w in UniversoMenosL4:
    estado=s4
    for c in w:
        estado = delta4( estado , c )
    if estado in F4:
        print(w,"si esta en el lenguaje")
    else:
        print (w,"no esta en el lenguaje")

