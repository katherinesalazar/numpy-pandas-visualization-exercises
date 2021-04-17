#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
print(plt)

import math as math
print(math)

import numpy as np
print(np)

import pandas as pd
print(pd)


# In[4]:


# 1. Use matplotlib to plot the following equation: y = x**2 - x +2

x = range(-50, 50)
#the last "in x" need to point to the above ALWAYS
y = [n ** 2 - n + 2 for n in x]

plt.plot(x,y, c = 'pink')

plt.title('$y = x^2 - x + 2$', fontsize = 14)

plt.xlabel('x axis', fontsize = 14)
plt.ylabel('y axis', fontsize = 14)

plt.annotate('Origin', xy = (0,0), xytext = (0, 500), arrowprops ={})
plt.show()


# In[5]:


# 2 Create and label 4 separate charts for the following equations 
# (choose a range for x that makes sense):

x = range(100)
y1 = [math.sqrt(n) for n in x]
y2 = [n **3 for n in x]
y3 = [2**n for n in x]
y4 = [1/(n+1) for n in x]


# In[6]:


plt.figure(figsize = (10,8))
import math as math

# Plot 1
plt.subplot(2,2,1)
plt.plot(x,y1, color = 'red')
plt.title('$y = √x$')
#adding the show to show the graphs
plt.show()


# In[8]:


plt.figure(figsize = (10,8))
import math as math

# Plot 2
plt.subplot(2,2,2)
plt.plot(x,y2, color = 'orange')
plt.title('y2 = $x^3$')

#adding the show to show the graphs
plt.show()


# In[113]:


plt.figure(figsize = (10,8))
import math as math

# Plot 3
plt.subplot(2,2,3)
plt.plot(x,y3, color = 'green')
plt.title('y3 = $2^x$')

#adding the show to show the graphs
plt.show()


# In[114]:


plt.figure(figsize = (10,8))
import math as math

# Plot 4
plt.subplot(2,2,4)
plt.plot(x,y4, color = 'blue')
plt.title('y4= $1/(x+1)$')

#adding the show to show the graphs
plt.show()


# In[9]:


# 3 Combine the figures you created in the last step into 
# one large figure with 4 subplots.

plt.figure(figsize = (10,8))
import math as math

# Plot 1
plt.subplot(2,2,1)
plt.plot(x,y1, color = 'red')
plt.title('$y = √x$')

# Plot 2
plt.subplot(2,2,2)
plt.plot(x,y2, color = 'orange')
plt.title('y2 = $x^3$')

# Plot 3
plt.subplot(2,2,3)
plt.plot(x,y3, color = 'green')
plt.title('y3 = $2^x$')

# Plot 4
plt.subplot(2,2,4)
plt.plot(x,y4, color = 'blue')
plt.title('y4= $1/(x+1)$')

#adding the title
plt.suptitle('4 subplots')
#adding the show to show the graphs
plt.show()
plt.tight_layout()


# In[ ]:


# 4
# Combine the figures you created in the last step into 
# one figure where each of the 4 equations has a different 
# color for the points. 
# Be sure to include a legend and an appropriate title for the figure


# In[16]:


#Plot size of the actual print product

#defining the items for the 4 seperate charts below:
x = range(1,100)
y1 = [math.sqrt(n) for n in x]
y2 = [n **3 for n in x]
y3 = [2**n for n in x]
y4 = [1/(n+1) for n in x]



# Plot 1
plt.plot(x,y1, label ='$y = √x$', color = 'darkmagenta')

# Plot 2
plt.plot(x,y2, label = 'y2 = $x^3$', color = "pink")

# Plot 3
plt.plot(x,y3, label = 'y3 = $2^x$')

# Plot 4
plt.plot(x,y4, label = 'y4= $1/(x+1)$', color = "teal")


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Combined Figures from Last Step')
plt.ylim(0,20)
plt.xlim(1,20)
plt.legend()
plt.show()


# In[ ]:




