#Create a numpy array with random numbers.
#rand() - rand function is used to generate random numbers between 0 to 1.
import numpy as np
rand_array = np.random.rand(4)
print(rand_array)
# Create an 2d array with random number between 0 to 1.
rand_array_2d = np.random.rand(2,4)
print(rand_array_2d)
#randn() - randn function used to generate random numbers close to zero , this maybe return positive or negative.
randnArray = np.random.randn(5)
print(randnArray)
#The numpy.random.ranf() function is used in Python to generate random floating-point numbers 
# in the half-open interval [0.0, 1.0)(inclusive of 0.0, but exclusive of 1.0). 
# It is an alias for the numpy.random.random_sample() and numpy.random.random() functions.
ranfArray = np.random.ranf(4)
print(ranfArray)
#randint() - the function used to generate random integer in a given range.
# syntax - randintArray = np.random.randint(min,max,total_value)
randintArray = np.random.randint(1,20,10)
print(randintArray)