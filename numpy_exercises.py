#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
print(np)


# In[3]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[6]:


# 1. How many negative numbers are there?
# 4 negative numbers
len(a[a < 0])


# In[8]:


# 2. How many positive numbers are there?
# 5 negative numbers
len(a[a > 0])


# In[51]:


# 3. How many even positive numbers are there?
# 

#(a([a >0])) and (a[a % 2 == 0])


# In[97]:


a[a % 2 == 0], a[a > 0]


# In[100]:


# 4. If you were to add 3 to each data point,
# how many positive numbers would there be?
# 10 positive numbers
original_array = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
new4 = original_array + 3


# In[101]:


original_array = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
original_array + 3


# In[137]:


# 5. If you squared each number, 
# what would the new mean and standard deviation be?

import math as math
original_array = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
new_array = original_array **2
print(new_array)


# In[138]:


# mean of OG numbers
mean = np.mean(a)
print(mean)


# In[139]:


# standard deviation of OG numbers
std = np.std(a)
print(std)


# In[136]:


# mean of numbers new
meannew = np.mean(new_array)
print(mean)


# In[135]:


# standard deviation of new
stdnew = np.std(new_array)
print(std)


# In[87]:


# 6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.
#std numbers:
centering_array = [16, 100, 144, 529, 4, 1, 0, 0, 0, 36, 9, 49]
centering_new_array = new_array - mean
print(centering_new_array)


# In[ ]:





# In[103]:


#original numbers
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
centering_new_array6 = a - mean7
print(centering_new_array6)


# In[125]:


# 7. Calculate the z-score for each data point. 
# Recall that the z-score is given by:
#original values

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[130]:


zscore7 = (a - mean) / std
zscore7


# In[142]:


#Squared values z score

zscore5 = (new_array - meannew / stdnew )
zscore5


# # More NumPy 

# In[172]:


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of 
# all the numbers in above list

sum_of_a = np.sum(a)
sum_of_a


# In[167]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of 
# all the numbers in the above list

min_of_a = np.min(a)
min_of_a


# In[166]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of
# all the numbers in the above list

max_of_a = np.max(a)
max_of_a


# In[165]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of 
# all the numbers in the above list

mean_of_a = np.mean(a)
mean_of_a


# In[173]:


# Exercise 5 - Make a variable named product_of_a to hold the product 
# of multiplying all the numbers in the above list together

product_of_a = np.prod(a)
product_of_a


# In[176]:


# Exercise 6 - Make a variable named squares_of_a.It should hold each 
# number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = np.square(a)
squares_of_a


# In[190]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only 
# the odd numbers

odds_in_a = [n for n in a if n % 2 == 1]
odds_in_a


# In[ ]:


# Exercise 8 - Make a variable named evens_in_a. 
#It should hold only the evens.


# In[191]:


evens_in_a = [n for n in a if n % 2 == 0]
evens_in_a


# In[7]:


## What about life in two dimensions? A list of lists is matrix, 
## a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, 
## average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[8]:


# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable 
# is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)

b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])


# In[9]:


sum_of_b = b.sum()
sum_of_b


# In[200]:


# Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  


# In[204]:


min_of_b = b.min()
min_of_b


# In[206]:


# Exercise 3 - refactor the following maximum calculation to 
# find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
max_of_b


# In[207]:


# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = b.mean()
mean_of_b


# In[12]:


# Exercise 5 - refactor the following to use numpy for calculating the 
# product of all numbers multiplied together.

product_of_b = b.prod()
product_of_b


# In[211]:


# Exercise 6 - refactor the following to use numpy to find the 
# list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

squares_of_b = b**2
squares_of_b


# In[212]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

odds_in_b = b %2 != 0
odds_in_b


# In[213]:


# Exercise 8 - refactor the following to use numpy to filter only 
#the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

evens_in_b = b %2 == 0
evens_in_b


# In[8]:


# Exercise 9 - print out the shape of the array b.

arr = np.array(b)
print(arr.shape)


# In[14]:


# Another way to do b.shape
b.shape


# In[15]:


# Exercise 10 - transpose the array b.
b.transpose()


# In[15]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. 
# (1 x 6)

reshape = np.array(b).reshape((6))
print(reshape)


# In[ ]:





# In[18]:


# Exercise 12 - reshape the array b to be a list of 6 lists, 
# each containing only 1 number (6 x 1)

reshape = np.array(b).reshape((6,1))
print(reshape)


# # Setup 3

# In[18]:


c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# In[19]:


# HINT, you'll first need to make sure that the "c" variable 
# is a numpy array prior to using numpy array methods.

carray = np.array(c)
print(c)


# In[27]:


# Exercise 1 - Find the min, max, sum, and product of c.

#min
cmin = carray.min()
print(cmin)

#max
cmin = carray.max()
print(cmin)

#sum
cmin = carray.sum()
print(cmin)

#product
cmin = carray.prod()
print(cmin)


# In[28]:


# Exercise 2 - Determine the standard deviation of c.
cstd = np.std(carray)
print(cstd)


# In[32]:


# Exercise 3 - Determine the variance of c.
cvar = np.var(carray)
print(carray)


# In[33]:


# Exercise 3 - Determine the variance of c.
cvar = np.var(c)
print(c)


# In[34]:


# Exercise 4 - Print out the shape of the array c
carr = np.array(carray)
print(carr.shape)


# In[35]:


# Exercise 4 - Print out the shape of the array c
carr = np.array(c)
print(carr.shape)


# In[36]:


# Exercise 5 - Transpose c and print out transposed result.
ctrans = np.transpose(carray)
print(ctrans)


# In[21]:


# Exercise 5 - Transpose c and print out transposed result.
ctrans = np.transpose(c)
print(ctrans)


# In[42]:


# Exercise 6 - Get the dot product of the array c with c. 
cdot = np.dot(c,carray)
print(cdot)


# In[43]:


# Exercise 6 - Get the dot product of the array c with c. 
cdot = np.dot(carray,c)
print(cdot)


# In[23]:


# Exercise 7 - Write the code necessary to sum up the result of 
# c times c transposed. Answer should be 261 ???

csum = (ctrans * ctrans.transpose()).sum()
print(csum)


# In[51]:


# Exercise 8 - Write the code necessary to determine the product of 
# c times c transposed. Answer should be 131681894400.
cprod = np.prod(c * ctrans)
print(cprod)


# # Setup 4

# In[62]:


d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


# In[66]:


# Exercise 1 - Find the sine of all the numbers in d
dsin = np.sin(d)
print(dsin)


# In[67]:


# Exercise 2 - Find the cosine of all the numbers in d
dcos = np.cos(d)
print(dcos)


# In[69]:


# Exercise 3 - Find the tangent of all the numbers in d
dtan = np.tan(d)
print(dtan)


# In[78]:


#finding the array of d
darray = np.array(d)
print(d)


# In[80]:


# Exercise 4 - Find all the negative numbers in d
dnegative = darray[darray < 0]
print(dnegative)


# In[81]:


# Exercise 5 - Find all the positive numbers in d
dpositive = darray[darray > 0]
print(dpositive)


# In[84]:


# Exercise 6 - Return an array of only the unique numbers in d.
uniquenum = np.unique(darray)
print(uniquenum)


# In[85]:


# Exercise 7 - Determine how many unique numbers there are in d.
uniquenum = len(np.unique(darray))
print(uniquenum)


# In[87]:


# Exercise 8 - Print out the shape of d.
dshape = np.array(darray)
print(dshape)


# In[89]:


# Exercise 9 - Transpose and then print out the shape of d.
dtrans = np.transpose(darray)
print(dtrans)


# In[88]:


# Exercise 10 - Reshape d into an array of 9 x 2
dreshape = np.array(darray).reshape((9,2))
print(dreshape)

