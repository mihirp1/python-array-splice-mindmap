if __name__=="__main__":
 array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
 print(array[-2:])

#Nice way to Remember Positive and Negative Indexing
 '''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
   0   1   2   3   4   5 
  -6  -5  -4  -3  -2  -1
 '''
#Nice way to remember to extend 
 '''
 The answers above don't discuss multi-dimentional array slicing which is possible using the famous numpy package:

Slicing also apply to multi-dimentional arrays.

# Here, a is a numpy array

>>> a
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> a[:2,0:3:2]
array([[1, 3],
       [5, 7]]) 

  '''
