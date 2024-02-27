import ramdom

lista = []
for i in range (1,26 ) : 
    lista.append (ramdom.randint(1,6))
    
conceito = []
quantidade = []

conceito.append ('Excelente')
quantidade.append (lista.count (5))
conceito.append ('  Bom')
quantidade.append (lista.count (4))
conceito.append ('Regular')
quantidade.append (lista.count (3))
conceito.append ('Ruim')
quantidade.append (lista.count (2))
conceito.append ('Péssimo')
quantidade.append (lista.count (1))

MaiorQnt = quantidade[0]
MaiorCon = conceito [0]

if quantidade[i] >  MaiorQnt : 
    MaiorQnt = quantidade[i]
    MaiorCon = conceito [i]
