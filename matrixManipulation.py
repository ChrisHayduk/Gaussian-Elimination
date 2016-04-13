class Matrix(object):

        def __init__(self, A):
                self.matrix = A

                self.numRows = len(self.matrix)

                if self.numRows != 0:
                        self.numCols = len(self.matrix[0])

#Checks if the matrix is valid
#If not, raises and handles an exception. Also returns False

        def isMatrix(self):
                tOrF = True

                try:
                        for eachRow in self.matrix:
                                if len(eachRow) != self.numCols:
                                        tOrF = False
                                        raise ValueError

                except ValueError, IndexError:
                        print self.matrix, "is not a matrix"
                        raise ValueError

                finally:
                        return tOrF

#Checks if matrices can be added
#If not, raises and handles an exception. Also returns False

	def canAdd(self, B):
                tOrF = True

                try:
                        if(self.isMatrix() == True and B.isMatrix() == True):
                                if(self.numRows != B.numRowsB or self.numCols != B.numCols):
                                        tOrF = False
                                        raise ValueError
                        else:
                                tOrF = False
                                raise ValueError

                except ValueError:
                        print self.matrix, B.matrix, "cannot be added"
                        raise ValueError

                finally:
                        return tOrF

#Checks if matrices can be multiplied
#If not, raises and handles an exception. Also returns False

	def canMultiply(self, B):
                tOrF = True

                try:
                        if(self.isMatrix() == True and B.isMatrix() == True):
                                if(self.numCols != B.numRows):
                                        tOrF = False
                                        raise ValueError
                        else:
                                tOrF = False
                                raise ValueError

                except ValueError:
                        print self.matrix, B.matrix, "cannot be multiplied"
                        raise ValueError

                finally:
                        return tOrF

	def canAdd(self, B):
		tOrF = True
		
		try:
			numRowsA = len(self.matrix)
			numColsA = len(self.matrix[0])
		
			numRowsB = len(B.matrix)
			numColsB = len(B.matrix[0])
		
			if(numRowsA != numRowsB or numColsA != numColsB):
				tOrF = False
				raise ValueError
	
		except ValueError:
			print self.matrix, B.matrix, "cannot be added"
		
		finally:
			return tOrF

#Adds two matrices together

	def __add__(self, B):
                C = Matrix([])

                try:
                        if self.canAdd(B) == True:
                                for i in range(self.numRows):
                                        tempRow = []
                                        for j in range(B.numCols):
                                                tempRow.append(self.matrix[i][j]+B.matrix[i][j])
                                        C.matrix.append(tempRow)

                except ValueError, IndexError:
                        raise ValueError

                finally:
                        C.numRows = len(C.matrix)

                        if C.numRows != 0:
                                C.numCols = len(C.matrix[0])
                        else:
                                C.numCols = 0

                        return C

#Multiplies a matrix by a scalar quantity
#Overloades the multiplication operator
#Matrix must be on the right side of the equation

	def __rmul__(self, num):
                B = Matrix([])

                try:
                        for i in range (self.numRows):
                                tempRow = []
                                for j in range(self.numCols):
                                        tempRow.append(self.matrix[i][j]*num)
                                B.matrix.append(tempRow)

                except ValueError, IndexError:
                        raise ValueError

                finally:
                        B.numRows = len(B.matrix)
                        B.numCols = len(B.matrix[0])
                        return B

#Transposes a matrix

	def matrixTransposition(self):
		B = Matrix([])

		try:
                	for i in range (self.numCols):
                                tempRow = []
                                for j in range(self.numRows):
                                        tempRow.append(self.matrix[j][i])
                                B.matrix.append(tempRow)

                except ValueError, IndexError:
                        raise ValueError

                finally:
                        B.numRows = len(B.matrix)

                        if B.numRows != 0:
                                B.numCols = len(B.matrix[0])
                        else:
                                B.numCols = 0

                        return B

#Multiplies two matrices
#Overloades the multiplication operator

	def __mul__(self, B):
		D = Matrix([])

                try:
                        if self.canMultiply(B) == True:
                                C = B.matrixTransposition()

                                for row1 in self.matrix:
                                        tempRow = []
                                        for row2 in C.matrix:
                                                tempRow.append(self.dotProduct(row1, row2))
                                        D.matrix.append(tempRow)

                except ValueError:
                        raise ValueError

                finally:
                        D.numRows = len(D.matrix)

                        if D.numRows != 0:
                                D.numCols = len(D.matrix[0])
                        else:
                                D.numCols = 0

                        return D
		

#Raises a matrix to a power
#Overloades the power operator

	def __pow__(self, num):
		C = Matrix(self.matrix)

                try:
                        C.matrix = self.matrix

                        for i in range(num-1):
                                C = self * C

                except ValueError:
                        raise ValueError

                finally:
                        C.numRows = len(C.matrix)

                        if C.numRows != 0:
                                C.numCols = len(C.matrix[0])
                        else:
                                C.numCols = 0

                        return C


#Returns the dot product of two vectors

	def dotProduct(self, vector1, vector2):
		num = 0

		for x in range(len(vector2)):
			num = num + (vector1[x] * vector2[x])
	
		return num

#Converts matrix to a string so that it can be printed

	def __str__(self):
		string = ""

		for row in self.matrix:
			temp = str(row)
			string += "\n"
			string += temp
		
		string = string[1:]

		return string

#Gaussian Elimination operations

	def swapRows(self, num1, num2):
		A = Matrix(self.matrix)
		
		tempRow = A.matrix[num1]
		
		A.matrix[num1] = A.matrix[num2]
		A.matrix[num2] = tempRow
		
		return A
	
	def multiplyRow(self, row, num):
		A = Matrix(self.matrix)

		tempRow = []
		
		for i in A.matrix[row]:
			ans = float(i*num)
			tempRow.append(ans)
		
		A.matrix[row] = tempRow 
		
		return A
	
#Row 1 is the one that will be replaced
	
	def multiplyAndAddRows(self, row1, row2, num):
		A = Matrix(self.matrix)	
	
		tempRow1 = []
		tempRow2 = []
		
		for i in A.matrix[row2]:
			tempRow1.append(i * num)
		
		for x in range(A.numCols):
			tempRow2.append(A.matrix[row1][x] + tempRow1[x])
		
		A.matrix[row1] = tempRow2	

		return A

	def echelonForm(self):
		tempMatrix = self.matrixTransposition
		position = -1
		tOrF = True

		for i in range(self.numCols):
			if self.matrix[0][i] != 0:
				position = i
				break
	
		if position == -1:
			tOrF = False
		
		row = 0
		
		for y in range(self.numCols):
			position = position + y 
			row = row + 1

			if position == self.numCols or position > self.numCols or row == self.numRows:
				break

			for i in range(position+1):
				if self.matrix[row][i] != 0:
					tOrF = False
					return tOrF	
			

		return tOrF

	def submatrix(self, row, col):
		A = Matrix(self.matrix)
		B = Matrix([])

		for x in range(row, A.numRows):
			tempRow = []
			for i in range(col, A.numCols):
				tempRow.append(A.matrix[x][i])
			B.matrix.append(tempRow)
		
		return B
	
	def combine(self, B):
		A = Matrix(self.matrix)
		
		for x in range(B.numRows):
			for i in range(B.numCols):
				A.matrix[A.numRows-1-x][A.numCols-1-i] = B.matrix[B.numRows-1-x][B.numCols-1-i]
		
		return A

	def findLeadingNumber(self, r, c):
		col = -1
		row = -1

		for i in range(c, self.numCols):
			for x in range(r, self.numRows):
				if self.matrix[x][i] != 0:
					col = i
					row = x
					break
			if col == i:
				break
		
		return row, col	

	def makeLeadingEntryOne(self, row, col):
		num = self.matrix[row][col]

		if num != 1 and num != 0:
			fnum = float(num)
			multiple = 1.0/num
			self.multiplyRow(row, multiple)

	def zeroOut(self, row, col):
		for x in range(row+1, self.numRows):
			if self.matrix[x][col] != 0:
				num = -(self.matrix[x][col])
			
				self.multiplyAndAddRows(x, row, num)

#Gaussian Elimination using recursion

	def GE(self):
		A = Matrix(self.matrix)

		if A.numRows == 1:
			return A

		else:
			#Find the row and column of the leading entry
			row, col = A.findLeadingNumber(0, 0)
	
			#Swap rows so that leftmost number is in first row
			A.swapRows(row, 0)
			
			#Set leading entry to 1
			A.makeLeadingEntryOne(0, col)
			
			#Zero out all entries beneath leading entry
			A.zeroOut(0, col)

			#Get the submatrix of A
			B = A.submatrix(1, col+1)
			
			#Perform GE on submatrix
			C = B.GE()
			
			#Combine original matrix and submatrix
			A.combine(C)
			
		return A
			

#Gaussian Elimination without recursion
		
	def gaussianElimination(self):
		A = Matrix(self.matrix)

		row, col = A.findLeadingNumber(0, 0)

		A.swapRows(row, 0)

		row = 0
		
		while (row+1) < A.numRows:
			A.makeLeadingEntryOne(row, col)
			
			A.zeroOut(row, col)			
			
			row, col = A.findLeadingNumber(row+1, col)				
		return A	

if __name__ == '__main__':
	A = Matrix([[1,2],[3,4]])
	B = Matrix([[5,6],[7,8]])
	
	print 'Matrix A: '
	print A

	print '\nMatrix B: '
	print B
	
	#Test matrix addition

	C = Matrix([])

	C = A + B

	print '\nAddition matrix:'

	print C

	#Test matrix scalar multiplication

	C = -2 * A
	
	print '\nScalar multiplication matrix (A * -2):'

	print C

	#Test matrix transposition

	C = B.matrixTransposition()
	
	print '\nTransposition of matrix B:'

	print C

	#Test matrix multiplication

	C = A * B

	print '\nMultiplication matrix:'

	print C

	#Test raising matrix to a power
	
	C = A ** 3
	
	print '\nMatrix A to the third power:'	

	print C
