import time

def imprimir_musica_por_palavra(musica):
    palavras = musica.split(' ')
    for palavra in palavras:
        print(palavra, end=' ', flush=True)
        time.sleep(0.1)  
    print() 

musica = '''Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor

Os animaizinhos subiram de dois em dois
Os animaizinhos subiram de dois em dois
O elefante
E os passarinhos, como os filhos do Senhor

Os animaizinhos subiram de dois em dois
Os animaizinhos subiram de dois em dois
A minhoquinha
E os pinguins, como os filhos do Senhor

Os animaizinhos subiram de dois em dois
Os animaizinhos subiram de dois em dois
O canguru
E o sapinho, como os filhos do Senhor

Deus disse a Noé: Constrói uma arca
Deus disse a Noé: Constrói uma arca
Que seja feita
De madeira para os filhos do Senhor

Por isso...!
Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor

Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor

Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor

E atenção agora, porque

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda

Balança a cabeça
O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda

Balança a cabeça, dá uma voltinha
O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda
Balança a cabeça, dá uma voltinha
Dá um pulinho

O senhor tem muitos filhos
Muitos filhos ele tem
Eu sou um deles, você também
Louvemos ao senhor

Braço direito, braço esquerdo
Perna direita, perna esquerda
Balança a cabeça, dá uma voltinha
Dá um pulinho e abraça o irmão'''