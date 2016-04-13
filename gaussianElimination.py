from matrixManipulation import *

A = Matrix([[1, 2, 3], [4, 5, 6]])

print A, '\n'

X = A.swapRows(0, 1)

print X, '\n'

X = A.multiplyRow(0, 3)

print X, '\n'

X = A.multiplyAndAddRows(0, 1, 2)

print X, '\n'

tOrF = A.echelonForm()

print tOrF

B = Matrix([[1, 2, 1, 2], [0, 1, 1, 1], [0, 0, 1, 1]])

tOrF = B.echelonForm()

print tOrF, '\n'

C = Matrix([[1, 2, 1, 2], [2, 6, 1, 7], [1, 1, 4, 3]])

X = C.GE()

print X, '\n'

X = C.gaussianElimination()

print X, '\n'

D = Matrix([[0, 0, 0, 0], [0, -1, 1, -2], [0, 2, -2, 4], [0, 3, -3, 6]])

QW = D.GE()

print QW, '\n'

Z = Matrix([[2,3],[4,5]])

m = Z.GE()

print m, '\n'

ZA = Matrix([[3,7,21,5,9],[4,20,17,12,19],[1,8,7,4,23]])

m = ZA.GE()

print m, '\n'

m = ZA.gaussianElimination()

print m
