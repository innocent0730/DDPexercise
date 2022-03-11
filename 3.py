#!/usr/bin/env python
# coding: utf-8

# In[4]:


def number(a):
    upstrcount = []
    lowstrcount = []
    other = []
    for b in a:
        if b.isupper():
            upstrcount.append(b)
        elif b.islower():
            lowstrcount.append(b)
        else:
            other
    return upstrcount,lowstrcount
a = 'Hello World'
x,y = number(a)
print('Uppercase:{}'.format(len(x)))
print('Lowercase:{}'.format(len(y)))


# In[ ]:




