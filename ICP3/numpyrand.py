import numpy

array=  numpy.random.randint(20, size=15)
print("random array is",array)
#array2 = numpy.random.randint(20, size=(3,5))
array1 = array.reshape(3,5)
print("random array is",array1)

#replacing the maximum number in a matrix
replace = numpy.where(array1 == numpy.max(array1,axis=1).reshape(-1,1), 0 * array1, array1)

print('Replacing Max No by 0:', replace)

