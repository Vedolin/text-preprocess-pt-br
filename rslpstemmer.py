from nltk.stem import RSLPStemmer

arquivo = open('class/resultado.txt', 'r')
stemizado = open('class/stemm.txt', 'w')

st = RSLPStemmer()
stem = []

for linha in arquivo:
    linha = linha.split()
    l = []
    for palavra in linha:
        stm = st.stem(palavra)
        l.append(stm)
    print(l)
    stemizado.write(' '.join(l) + '\n')