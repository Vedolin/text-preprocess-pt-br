from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *

ocurrences = []

with open('class/resultado.txt') as f:
    occurrences = Counter(f.read().split()).most_common(50)

label = [i[0] for i in occurrences]
value = [i[1] for i in occurrences]

x_axis = label
y_axis = value

ind = np.arange(len(x_axis))
#print(ind)

my_dpi = 100
plt.figure(figsize=(800/my_dpi, 500/my_dpi), dpi=my_dpi)
plt.bar(ind, y_axis, color='Firebrick', )
plt.xticks(ind, x_axis, rotation='75', size='small', color = 'navy')
plt.yticks(color='navy', size='small')
plt.subplots_adjust(bottom=0.2) #ajusta parte de baixo do gráfico na tela
plt.tick_params(width=1) #traço nos labels
plt.title("Ocorrência de Palavras", color='navy')
plt.xlabel('Palavras')
plt.axhline(30, color="gray", linestyle='--', marker='s', linewidth=0.5)
plt.axhline(25, color="gray", linestyle='--', marker='s', linewidth=0.5)
plt.axhline(15, color="gray", linestyle='--', marker='s', linewidth=0.5)
plt.axhline(20, color="gray", linestyle='--', marker='s', linewidth=0.5)
plt.axhline(10, color="gray", linestyle='--', marker='s', linewidth=0.5)
plt.axhline(5, color="gray", linestyle='--', marker='s', linewidth=0.5)
plt.ylabel('Frequência')
plt.show()
