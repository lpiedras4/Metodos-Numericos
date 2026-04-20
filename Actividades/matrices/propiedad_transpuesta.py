import numpy as np

def multiplicacion_matricial (A, b):
  c = [[0]*len(b[0]) for _ in range(len(A))]

  for i in range(len(A)):
    for j in range(len(b[0])):
      for k in range(len(b)):
        c[i][j] += A[i][k] * b[k][j]
  
  return c



A1=[
  [1, 2],
  [0, 3]
]

B1=[
  [4, -1],
  [2, 1]
]

#Calcular AB y luego transponer (AB)^T
C1 = multiplicacion_matricial(A1,B1)
C1 = np.transpose(C1)
print(C1)
#Calcular B^T y A^T por separado y multiplicar  B^T * A^T
Bt = np.transpose(B1)
At = np.transpose(A1)
C2 = multiplicacion_matricial( Bt,At )
print(C2)



