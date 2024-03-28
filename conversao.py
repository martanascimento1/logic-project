def traduzir_para_logica(sentenca):
    # Substituições para as palavras-chave
    sentenca = sentenca.replace("E", "and")
    sentenca = sentenca.replace("OU", "or")
    sentenca = sentenca.replace("ENTÃO", "->")
    sentenca = sentenca.replace("É falso que", "~")

    # Imprime a sentença traduzida
    return sentenca

# Exemplos de sentenças em linguagem natural
p = "Chove em Curitiba"
q = "uso guarda-chuva"

sentenca1 = f"{p} E {q}"
sentenca2 = f"Tweety é um pássaro OU Tweety é um mamífero"
sentenca3 = f"Se {p} ENTÃO {q}"
sentenca4 = f"É falso que Tweety é um mamífero"

# Traduzindo as sentenças
print(traduzir_para_logica(sentenca1))  # Output: p and q
print(traduzir_para_logica(sentenca2))  # Output: r or s
print(traduzir_para_logica(sentenca3))  # Output: r -> u
print(traduzir_para_logica(sentenca4))  # Output: ~u
