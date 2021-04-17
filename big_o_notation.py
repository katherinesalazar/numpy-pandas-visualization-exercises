#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import math as math
import numpy as np
import pandas as pd

#defining the items for the curves to graphs below:
x = list(range(1,20)) 
y1 = [1 for n in x] 
y2 = [math.log(n) for n in x]
y3 = x
y4 = [(n * math.log(n))for n in x]
y5 = [n**2 for n in x]
y6 = [2**n for n in x]
y7 = [math.factorial(n) for n in x]
y8 = [n^n for n in x]


# In[6]:


#Plot size of the actual print product
plt.figure(figsize = (16,8))

#title naming
plt.title('Big O Notation')
#x axis naming
plt.xlabel('Elements')
#y axis naming
plt.ylabel('Operations')


# Plot 1
plt.plot(x,y1, color = 'red', label='$O(1)$', alpha=.2) 

# Plot 2
plt.plot(x,y2, color = 'orange', label='$O(log n)$', alpha=.3) 

# Plot 3
plt.plot(x,y3, color = 'green', label='$O(n)$', alpha=.4) 

# Plot 4
plt.plot(x,y4, color = 'blue', label='$O(n log n)$', alpha=.5) 

# Plot 5
plt.plot(x,y5, color = 'red', label='$O(n^2)$', alpha=.6) 

# Plot 6
plt.plot(x,y6, color = 'pink', label='$O(2^n)$', alpha=.7) 

# Plot 7
plt.plot(x,y7, color = 'teal', label='$O(n!)$', alpha=.8 ) 

# Plot 8
plt.plot(x,y8, color = 'yellow', label='$O(n^n)$', alpha=.9 ) 

plt.xlim(1, 11)
plt.ylim(0, 50)

#making a legend for curves
plt.legend()
#adding the show to show the graphs
plt.show()


# In[ ]:





# In[ ]:




