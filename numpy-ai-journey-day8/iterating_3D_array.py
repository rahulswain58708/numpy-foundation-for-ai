import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr: #it will go through all 2D Array
    for y in x: #it will go through all row inside 2D Array
        for z in y: #it access each element in a row
            print(z) #display element