import numpy as np

arr = np.array([1,2,3,4,5])

print("Soma: ", np.sum(arr))
print("Média: ", np.mean(arr))
print("Desvio padrao: ", np.std(arr))

matriz = np.array([[1,2], [3,4]])
print("Determinante: ", np.linalg.det(matriz))      