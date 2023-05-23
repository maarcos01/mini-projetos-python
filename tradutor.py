from translate import Translator

def en_pt(frase):
    linguas = Translator(from_lang='english', to_lang='portuguese')
    tradutor = linguas.translate(frase)

    return print(tradutor)

r = 'S'
while r == 'S':
    frase = str(input('Digite a frase que quer traduzir: '))
    en_pt(frase)
    r = str(input('Quer traduzir outra frase S/N:')).upper().strip()