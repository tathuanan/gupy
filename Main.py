### Variáveis Globais - INÍCIO ###
falas_do_cantor_originais = { 
    1 : '(Para não!)',
    2 : '(de novo!)',
    3 : '(Até que eu tô em forma)',
    4 : '(muitos filhos)',
    5 : '(Que saudade dessa música)',
    6 : '(Bonita cruz)',
    7 : '(Para não)',
}
    
partes_do_corpo_originais = {
    1 : 'braço',
    2 : 'perna',
    3 : 'a cabeça',
}

animais_originais = [
    ['O elefante', 'E os passarinhos'],
    ['A minhoquinha', 'E os pinguins'],
    ['O canguro', 'E o sapinho'],
]
### Variáveis Globais - FIM ###

### Importando Módulos ###
FUNCTIONS = __import__('Functions')

if __name__ == "__main__":
    FUNCTIONS.menu_reproduzir_musica()