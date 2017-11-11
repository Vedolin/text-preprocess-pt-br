from unicodedata import normalize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
arquivo = open('processar.txt', 'r')
resultado = open('resultado.txt', 'w')

for linha in arquivo:
    # ----Transformando caracteres em letras MINUSCULAS----#
    linha = linha.lower()

    # ----Trasnformando ABREVIAÇÕES----#
    i = 0
    abv = ['blz', 'flw', 'vlw', ' ta ', ' mt ', ' q ', ' n ', ' pq ', ' ok ', ' vcs ', ' vc ', ' amr ', ' migo ',
           'migs', 'hj', 'tmb', 'oq', ' br ', 'eua']
    abv2 = ['beleza', 'tchau', ' obrigado ', ' esta ', ' muito ', ' que ', ' nao ', ' porque ', ' entendi ', ' voces ',
            'voce', ' amor ', 'amigo', 'amigo', 'hoje', 'tambem', 'o que', 'brasil', 'estados unidos da america']
    while i < len(abv):
        linha = linha.replace(abv[i], abv2[i])
        i = i + 1

    # ----Transformando EMOTICONS em palavras----#
    i = 0
    emt = ['(:', ':)', '=)', '(=', ':D', 'D:', ';)', '(;', ' xd ', ':O', ':P', '<2', '<3', '><', ' s2 ', ' sz ', 'u.u',
           ':@', ':/', ":'(", ':9', ':x', '*-*']
    emtC = ['sorrindo', 'sorrindo', 'sorrindo', 'sorrindo', 'sorrindo', 'surpreso', 'piscando', 'piscando', 'sorrindo',
            'surpreso', 'lingua de fora', 'amor', 'amor', 'gostei', 'amor', 'amor', 'prevalecido', 'bravo', 'indeciso',
            'chorando', 'gostando', 'aborrecido', 'gostando']
    while i < len(emt):
        linha = linha.replace(emt[i], emtC[i])
        i = i + 1

    # ---- STOPWORDS ----#
    stop_words = set(stopwords.words("portuguese"))
    stop_words.update(['nao', 'voces', 'ficam', 'tirar', 'sobre', 'quer', 'querem', 'vou', 'vamos', 'ir', 'gente', 'fazer', 'cada', 'acho', 'pode', 'cara', 'bem', 'pois', 'ninguem', 'ainda', 'mae', 'deve', 'estado', 'pai', 'filhos', 'filho','porque', 'pais', 'anos', 'nunca', 'casa', 'pessoas','nessa', 'algum', 'algumas', 'nesse', 'aqui', 'coisa', 'seria', 'pros', 'poxa', 'ser', 'assim', 'dar', 'fez', 'quiser', 'posso', 'todo', 'toda', 'nada', 'todos', 'ninguem', 'etc', 'ter', 'la', 'ate', 'faz', 'ficar','ai', 'vai', 'pega', 'vao', 'e', 'pra', 'sim', 'ta', 'vi', 'vem', 'pro', 'tambem', 'hoje', 'pede'])
    ##descomente a linha abaixo para ver a lista de stopwords##
    # print(stop_words)
    words = word_tokenize(linha)
    ##descomente a linha abaixo para ver os tokens criados##
    # print(words)
    linha_limpa = [w for w in words if not w in stop_words]
    linha = str(''.join(str(e + ' ') for e in linha_limpa))

    # ----Removendo ACENTUAÇÃO ----#
    linha = normalize('NFKD', linha).encode('ASCII','ignore').decode('ASCII')

    # ----Removendo CARACTERES ESPECIAIS ----#
    i = 0
    caracteres = [ ' sera ', ' agora ', ' so ', ' ja ', ' sao ', ' ta ', ' ai ',' e ', ', ', '. ', '? ', '! ', '`', "'", '@', '*', '#', '%', '¨', '-', '_', '+', '-', '=', ')', '(', '[', ']', '.', '&', ':', '>', '<']
    while i < len(caracteres):
        linha = linha.replace(caracteres[i], " ")
        i = i + 1



    #---- ESCREVE linha processada em resultado.txt ----#
    resultado.write(linha+'\n')

arquivo.close()
resultado.close()

