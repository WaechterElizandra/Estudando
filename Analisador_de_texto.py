#desenvolva um analisador de texto que identificaca palavras frequentes, conta caracteres e palavras
# e calcula a densidade de palavras-chave
from collections import Counter #subclasse dict para contar objetos com hash. é utilizado para identificar o bloco de dados único, mas também para criar “links” entre cada bloco de dados
import re #Este módulo fornece operações de correspondência de expressões regulares

def analisador_de_texto(texto, palavra_chave):
    #contando caracteres
    total_caracteres = len(texto)

    #contando palavras
    palavras = re.findall(r'\w+', texto.lower())
    total_palavras = len(palavras)

    #contagem de palavras frequentes
    contador_palavras = Counter(palavras)
    palavras_frequentes = contador_palavras.most_common(5) # o número determina mais ou menos palavras

    #calculo de densidade de palavras-chave
    palavras_chave_encontradas = [palavra for palavra in palavras if palavra in palavra_chave]
    densidade_de_palavras_chave = (len(palavras_frequentes)/total_palavras) * 100

    #resultados
    print("---- Resultados ----")
    print("Total de caracteres:", total_caracteres)
    print("Total de palavras:", total_palavras)
    print("Palavras frequentes:")
    for palavra, frequencia in palavras_frequentes:
        print(palavra, "-", frequencia, "vezes")
    print("Densidade de palavras-chave: %.2f%%" % densidade_de_palavras_chave)
texto= input('Informe o texto a ser analisado: ')


resul = analisador_de_texto(texto,texto)

