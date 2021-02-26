#!/usr/bin/env python
# coding: utf-8

# In[2]:


#for loop used for literating over a sequence and works more like a iterator method
fruits = ['apple' , 'orange' ,'banana']
for x in fruits:
    print(x)


# In[5]:


for x in "banana":
    print(x)


# In[10]:


#break with this statement we can stop the loop before it has looped all the item
fruits =['apple','banana', 'cherry']
for x in fruits:
    print(x)
    if x == "banana":
        break


# In[11]:


#break statement comes before the print
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == "banana":
        break
    print(x)


# In[13]:


#continue statement 
cars = ['ford', 'audi', 'bmw']
for x in cars:
    if x == "audi":
        continue
    print(x)


# In[14]:


#Range in for loop
for x in range(6):
    print(x)


# In[16]:


for x in range(2,8,2):
    print(x)


# In[17]:


#Else in for loop
for x in range(6):
    print(x)
else:
    print("Finished")


# In[19]:


#Else with break statement
for x in range(6):
    if x == 3: break
    print(x)
else:
    print('finally done')


# In[20]:


#nested loop the inner loop will be executed only once for each iteration of the "outer loop"

a = ["asd" ,"we", 12]
b = ["qw", "vgf", "gdfg"]

for x in a:
    for y in b:
        print(x,y)


# In[ ]:


#pass statement for some reaso you want to use for loop, but inside the loop there is no content at that time you can use for loop to avoid error


# In[21]:


#python function, a function is a block of code which runs only when it is called. you can pass data inside the function
def my_func():
    print('my function')
my_func()


# In[22]:


#function arguments, we can pass information to function as an arguments inside parentheses

def my_fun(temp):
    print(temp + "references")
my_fun("emil")
my_fun('Linuc')


# In[24]:


#passing two arguments inside a function. by default functions must be called with the correct number of arguments.
def hello(abc,tree):
    print(abc + "" + tree)
hello('email', 'qwe')


# In[25]:


x = 4
y = "sally"
print(x)
print(y)


# In[26]:


print(10 + 5)


# In[48]:


#multiple arguments
def my_fun(args):
    print("hello",args)
my_fun("this")


# In[47]:


#keyword arguments
def my_fun(test, test1, test2):
    print("the youngest child is " + test1)
my_fun(test="rahul", test1="raj", test2="raja")


# In[51]:


#multiple keyword arguments
def my_fun(**kid):
    print('his last name is ' + kid["lname"])
my_fun(fname = 'abc', lname = 'cde')


# In[52]:


#Default parameter value
def fun(test1 = "rahul"):
    print("I am from" + test1)
fun("pink")
fun()
fun('ghf')


# In[56]:


#passing list as a datatype
def fun(food):
    for x in food:
        print(x)
fruits = ['apple', 'orange', 'grapes']
fun(fruits)


# In[ ]:


#pass statement in function. It is used when function is empty and to avoid error.


# In[60]:


#Function Recursion Function calling itself
def fun(k):
    if(k>0):
        result = k + fun(k-1)
        print(result)
    else:
        result = 0
    return result
print('this is it')
fun(6)


# In[61]:


#python lambda its a anonymous function which is not stored but its associated with variable
x = lambda a : a + 10
print(x(5))


# In[62]:


#multiple arguments in lambda function
a = lambda x , y : x * y
print(a(5,4))


# In[64]:


x = lambda a, b, c :a + b + c
print(x(5,4,3))


# In[65]:


#function argument multiplied by unknown number
def fun(n):
    return lambda a : a * n
mydoubler = fun(2)
print(mydoubler(11))


# In[66]:


#make use of same defination to make both function in the same group
def my_fun(n):
    return lambda a : a * n
mydoubler = my_fun(2)
mytripler = my_fun(3)

print(mydoubler(11))
print(mytripler(11))


# In[70]:


#Python Class .. Creating a class
class MyClass:
    x = 5
print(MyClass)


# In[71]:


p1 = MyClass()
print(p1.x)


# In[81]:


#python class init() function
class person:
  def _init_ (self, name, age):
        self.name = name
        self.age = age
p1 = person('raj', 32)
print(p1.name)
print(p1.age)


# In[ ]:


#self parameter is the reference to the current instance of the class, and use to access variable that belong to the class


# In[75]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# In[83]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# In[86]:


#Creating a class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()


# In[89]:


#using class we are going to add properties
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

