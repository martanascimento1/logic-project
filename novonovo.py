import nltk
from nltk.corpus import wordnet as wn
from nltk.parse import stanfordcorenlp
from nltk.parse.corenlp import StanfordCoreNLPParser
from stanfordcorenlp import StanfordCoreNLP


# Dicionário de palavras-chave para conectivos lógicos
CONNECTIVES = {
    "e": "∧",
    "ou": "∨",
    "se": "→",
    "se...então": "→",
    "só se...então": "↔",
    "não": "¬",
}

# Dicionário de palavras-chave para quantificadores
QUANTIFIERS = {
    "todo": "∀",
    "algum": "∃",
}

# Função para converter uma frase em uma fórmula lógica
def to_logical_form(sentence):
    # Tokenizar a frase
    tokens = nltk.word_tokenize(sentence)

    # Identificar os conectivos lógicos
    connectives = [token for token in tokens if token in CONNECTIVES]

    # Identificar os quantificadores
    quantifiers = [token for token in tokens if token in QUANTIFIERS]

    # Identificar os substantivos
    nouns = [token for token in tokens if nltk.pos_tag([token])[0][1] == 'NN']

    # Identificar os verbos
    verbs = [token for token in tokens if nltk.pos_tag([token])[0][1] == 'VB']

    # Gerar a fórmula lógica
    formula = ""
    for i, token in enumerate(tokens):
        if token in CONNECTIVES:
            formula += CONNECTIVES[token]
        elif token in QUANTIFIERS:
            formula += QUANTIFIERS[token]
        elif token in nouns:
            # Obter o synset do WordNet
            synset = wn.synsets(token)[0]
            # Usar a primeira definição como rótulo da variável
            formula += synset.definition().split(';')[0]
        elif token in verbs:
            # Usar a primeira pessoa do singular do presente do indicativo
            verb_form = nltk.WordNetLemmatizer().lemmatize(token, 'v')
            formula += verb_form + 's'

    return formula

# Exemplo de uso
sentence = "Todo homem é mortal."
logical_form = to_logical_form(sentence)

print(f"Frase: {sentence}")
print(f"Fórmula lógica: {logical_form}")
