import numpy

print(numpy.poly([-1, 1, 1, 10]))       #Output : [  1 -11   9  11 -10]
# returns the coefficients of a polynomial with the given sequence of roots

print(numpy.roots([1, 0, -1]))          #Output : [-1.  1.]
# returns the roots of a polynomial with the given sequence of coefficients

print(numpy.polyint([1, 1, 1]))          #Output : [ 0.33333333  0.5         1.          0.        ]
# returns the antiderivative/integral of a polynomial given the coefficients

print(numpy.polyder([1, 1, 1, 1]))       #Output : [3 2 1]
#returns the derivative of a polynomial given the coefficients

print(numpy.polyval([1, -2, 0, 2], 4))   #Output : 34
# evaluates a polynomial at the given value

print(numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)) #Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]
# fits a polynomial of a specified order to a set of data using a least-squares approach

# The functions polyadd, polysub, polymul, and polydiv also handle proper
# addition, subtraction, multiplication, and division of polynomial coefficients, respectively