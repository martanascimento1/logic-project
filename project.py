def traduzir_para_logica_proposicional(sentencas):
    variaveis = {}

    # Solicitar ao usuário para inserir as palavras-chave e suas representações
    while True:
        palavra_chave = input("Digite uma palavra-chave (ou 'fim' para encerrar): ")
        if palavra_chave.lower() == "fim":
            break
        variavel = input(f"Qual variável proposicional representa '{palavra_chave}'? ")
        variaveis[palavra_chave] = variavel

    # Traduzir cada sentença em linguagem natural para linguagem lógica proposicional
    sentencas_logicas = []
    for sentenca in sentencas:
        for palavra, variavel in variaveis.items():
            sentenca = sentenca.replace(palavra, variavel)
        sentencas_logicas.append(sentenca)

    return sentencas_logicas

# Exemplo de uso
quantidade = int(input("Digite a quantidade de sentenças: "))
sentencas_naturais = []
for i in range(quantidade):
    sentenca_natural = input(f"Digite a {i+1}ª sentença em linguagem natural: ")
    sentencas_naturais.append(sentenca_natural)

sentencas_logicas = traduzir_para_logica_proposicional(sentencas_naturais)
for i, sentenca_logica in enumerate(sentencas_logicas):
    print(f"Sentença {i+1} em linguagem lógica proposicional: {sentenca_logica}")