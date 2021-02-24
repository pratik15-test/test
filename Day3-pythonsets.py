#!/usr/bin/env python
# coding: utf-8

# In[5]:


#set can be of any datatype
set1 = {'a' , 'c' , 'b'}
set2 = {'1' , '2' , '3'}
set3 = {True , False , True }
print(type(set1))


# In[7]:


set = (('hgf', 'jhg'))
print(set)


# In[9]:


#update a set from previous set
set2.update(set1)
print(set2)


# In[10]:


thisset = {'cat' , 'dog' , 'mouse'}
thiset1 = ['orange' , 'mango']
thisset.update(thiset1)


# In[12]:


thisset


# In[13]:


x = thisset.pop()
print(x)


# In[14]:


set23 = {'apple' , 'banana' , 'mango'}
set23.add('orange')


# In[15]:


set23


# In[16]:


thiset1 = {'asd' , 'qwe' , 'abc'}
tropical = {'mango' , 'papaya'}
thiset1.update(tropical)
print(thiset1)


# In[17]:


#adding iterable (list & set)
mylist = ['asd' , 'saw']
myset = {'dfg' , 'was'}
myset.update(mylist)


# In[18]:


myset


# In[20]:


myset


# In[23]:


#delete data item in set
thiset = {'apple' , 'cat' , 'grapes'}
thiset.remove('cat')
print(thiset)


# In[24]:


#poping single item from a set
x = thiset.pop()
print(x)


# In[25]:


print(thiset)


# In[26]:


#Clear all data from the set
thiset.clear()
print(thiset)


# In[31]:


#delete the list and error occurs while printing the set
myset = {'dd'}
del myset


# In[34]:


#Adding two sets using union
set4 = {'lets' , 'teach' , 'rohit'}
set5 = {'basketball'}
set6 = set4.union(set5)
print(set6)


# In[36]:


#Adding two sets using update
your = {'this' , 'is'}
mine = {'it'}
your.update(mine)
print(your)


# In[39]:


#Keep only the duplicates intersection_update
x ={'apple' , 'orange' , 'cherry'}
y = {'apple' , 'banana'}
x.intersection_update(y)
print(x)


# In[38]:


#intersection method
z =x.intersection(y)
print(z)


# In[43]:


#Items present in both the set (symmetric difference)
a = {'abc' , "def" , 'ghi'}
b = {'abc' , 'zxc' , 'lmn'}
a.symmetric_difference_update(b)
print(a)


# In[44]:


#symmetric difference method
w = {'car' , 'bike' , 'ford'}
e = {'car'}
v = w.symmetric_difference(e)
print(v)


# In[47]:


#Range of negative values (tuples)
set = ('orange' , 11 , 1.0 , 'sd' , 'cdf' , 'sf')
print(set[-3:-1])


# In[58]:


#Finding an item present in the list
thistuple = ("Ironman", "banana", "cherry")
if "Ironman" in thistuple:
  print("I Am Ironman")


# In[59]:


#Convert tuple into list
tuple1 = ('aq' , 'ant' , 'orange')
y = list(tuple1)
y[1] = 'kiwi'
tuple1 = tuple(y)
print(tuple1)


# In[63]:


#
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# In[ ]:




