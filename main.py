import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
from queue import PriorityQueue


lucros = np.array([50, 40, 70])  # Lucro por unidade de A, B, C
recursos = np.array([  # Consumo de recursos por unidade de A, B, C
    [2, 1, 3],  # Energia
    [1, 2, 1],  # Insumo químico X
    [1, 1, 2]   # Insumo químico Y
])
limites_recursos = np.array([100, 80, 90])  # Limites de recursos disponíveis

# Restrições do problema de otimização
# Minimização de lucros 
c = -lucros  
A_ub = recursos  # Matriz de restrições (consumo de recursos)
b_ub = limites_recursos  # Limites superiores dos recursos

# Restrições de não-negatividade para a produção
bounds = [(0, None), (0, None), (0, None)]


resultado = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')


if resultado.success:
    producao_otima = resultado.x
    lucro_maximo = -resultado.fun
    print("Produção ótima (unidades):", producao_otima)
    print("Lucro máximo (em unidades monetárias):", lucro_maximo)
else:
    print("Não foi possível encontrar uma solução ótima.")

# Visualização dos resultados
compostos = ["A", "B", "C"]
plt.bar(compostos, producao_otima, color=['blue', 'orange', 'green'])
plt.title("Distribuição Ótima de Produção")
plt.xlabel("Compostos")
plt.ylabel("Unidades Produzidas")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Estrutura de dados: Fila de prioridades para ordem de produção
fila_prioridade = PriorityQueue()
for i, lucro_unitario in enumerate(lucros):
    fila_prioridade.put((-lucro_unitario, compostos[i]))  # Lucro negativo para ordem decrescente

print("\nOrdem de produção por prioridade de lucro:")
while not fila_prioridade.empty():
    lucro, composto = fila_prioridade.get()
    print(f"Composto: {composto}, Lucro por unidade: {-lucro}")