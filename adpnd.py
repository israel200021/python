#L = { a^n b^n | n>0 }
print("ADPND 1 : L = { a^n b^n | n>0 }")
Q=['q1','q2','q3','q4']
Sigma=['a','b']
Gamma=['A','B']
s='q1'
z='A'
F=['q4']

DELTA = { ('q1','a','A') : ('q2','BA'),
          ('q2','a','B') : ('q2','BB'),
          ('q2','b','B') : ('q3',''),
          ('q3','b','B') : ('q3',''),
          ('q3','','A') : ('q4','A')
          }

pila=[z]

def transicion( q , sigma , gamma ):
    global pila
    p,w = DELTA[(q,sigma,gamma)]
    pila = list(w) + pila
    print("DELTA[",(q,sigma,gamma),":",DELTA[(q,sigma,gamma)])
    print("pila:",pila)
    return p

L =  [ 'ab','aabb','aaaabbbb' ]

for c in L:
    estado=s
    for x in c:
        gamma = pila.pop(0)
        estado = transicion( estado , x , gamma)
    gamma = pila.pop(0)
    estado = transicion( estado , '' , gamma )
    if estado in F:
        print(c , "SI esta en el lenguaje")
    else:
        print(c , "NO esta en el lenguaje")
 

#L = { w = {a,b}* | w tiene el mismo número de a's que de b's }
print("ADPND 2 : L = { w = {a,b}* | w tiene el mismo número de a's que de b's }")
Q = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']
Sigma = ['a', 'b']
Gamma = ['A', 'B']
s = 'q1'
z = 'A'
F = ['q4', 'q7']

DELTA = {('q1', 'a', 'A'): ('q2', 'BA'),
         ('q2', 'a', 'B'): ('q2', 'BB'),
         ('q2', 'b', 'B'): ('q3', ''),
         ('q3', 'b', 'B'): ('q3', ''),
         ('q3', 'b', 'A'): ('q5', 'BA'),
         ('q3', '', 'A'): ('q4', 'A'),
         ('q3', 'a', 'A'): ('q2', 'BA'),
         ('q1', 'b', 'A'): ('q5', 'BA'),
         ('q5', 'b', 'B'): ('q5', 'BB'),
         ('q5', 'a', 'B'): ('q6', ''),
         ('q6', 'b', 'A'): ('q5', 'BA'),
         ('q6', 'a', 'B'): ('q6', ''),
         ('q6', '', 'A'): ('q7', 'A'),
         ('q6', 'a', 'A'): ('q2', 'BA')
         }


pila = [z]

def transicion(q, sigma, gamma):
    global pila
    p, w = DELTA[(q, sigma, gamma)]
    pila = list(w) + pila
    print("DELTA[", (q, sigma, gamma), ":", DELTA[(q, sigma, gamma)])
    print("pila:", pila)
    return p

L = ['baba', 'abba', 'abab']

for c in L:
    estado = s
    for x in c:
        gamma = pila.pop(0)
        estado = transicion(estado, x, gamma)
    gamma = pila.pop(0)
    estado = transicion(estado, '', gamma)
    if estado in F:
        print(c, "SI esta en el lenguaje")
    else:
        print(c, "NO esta en el lenguaje")

#versin 2: ADPND 2
print("version 2 ADPND 2 : L = { w = {a,b}* | w tiene el mismo número de a's que de b's }")
Q=['q1','q2']
Sigma=['a','b']
Gamma=['A','B']
s='q1'
z='Z'
F=['q2']
DELTA = { ('q1','a','Z') : ('q1','AZ'),
          ('q1','b','Z') : ('q1','BZ'),
          ('q1','a','A') : ('q1','AA'),
          ('q1','b','B') : ('q1','BB'),
          ('q1','a','B') : ('q1',''),
          ('q1','b','A') : ('q1',''),
          ('q1','','Z') : ('q2','Z')
          }

pila=[z]

def transicion( q , sigma , gamma ):
    global pila
    p,w = DELTA[(q,sigma,gamma)]
    pila = list(w) + pila
    print("DELTA[",(q,sigma,gamma),":",DELTA[(q,sigma,gamma)])
    print("pila:",pila)
    return p

L =  [ 'ab','abba','baba' ]

for c in L:
    estado=s
    for x in c:
        gamma = pila.pop(0)
        estado = transicion( estado , x , gamma)
    gamma = pila.pop(0)
    estado = transicion( estado , '' , gamma )
    if estado in F:
        print(c , "SI esta en el lenguaje")
    else:
        print(c , "NO esta en el lenguaje")
 
