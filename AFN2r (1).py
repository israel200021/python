from itertools import chain, combinations

def conjunto_potencia(iterable):
    s=list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

Q=['q0','q1', 'q2', 'q3','q4']
s=['q0']
F=['q4']

DELTA={
  ('q0','0'):['q0'],
  ('q0','1'):['q0','q1'],
  ('q1','0'):['q2'],
  ('q1','1'):['q2'],
  ('q2','0'):['q3'],
  ('q2','1'):['q3'],
  ('q3','0'):['q4'],
  ('q3','1'):['q4'],
  ('q4','0'):[],
  ('q4','1'):[]
}

Qprima=list(conjunto_potencia(Q))
print();
sprima=('q0',)
Fprima=[]
Sigma=['0','1']

Sigmaprima=Sigma

print("Construyendo Fprima")
for X in Qprima:
  print(X)
  for q in X:
    print(q)
    if q in F:
      Fprima.append(X)

print("Qprima: ",Qprima)
print("sprima: ", sprima)
print ("Fprima: ",Fprima)

global delta
delta={}

for X in Qprima:
  for s in Sigmaprima:
    estados_sig=[]
    for q in X:
      estados_q_s = DELTA[(q,s)]
      for m in estados_q_s:
        if not(m in estados_sig):
          estados_sig.append(m)
      estados_sig.sort()
      delta[(X,s)]=tuple(estados_sig)

print("delta: ",delta)



def transicion(X,s):
    global delta, Sigmaprima
    STATUS = True
    if not(s in Sigmaprima):
        print(s, "no esta en el alfabeto")
        STATUS = False
        return STATUS
        #return STATUS, ''

    estados_sig = delta[(X,s)]
    print("Transicion(",X,",",s,")->" , estados_sig)
    STATUS = True
    return STATUS, estados_sig

w=['000011111','1000','11','1111']

for cadena in w:
    estado = sprima
    for l in cadena:
        print("ESTADO", estado)
        STATUS, estado = transicion(estado,l)

    if STATUS and estado in Fprima:
        print(cadena, "si está en el lenguaje")
        print()
    else:
        print(cadena,"no esta en el lenguaje")
        print()