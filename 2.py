#!/usr/bin/env python
# coding: utf-8

# In[16]:


def unique_letters(str):
    str = str.upper()
    Hello_World = []
    for char in str:
        if ((char.isalpha()) and (char not in Hello_World)):
            Hello_World.append(char)

    return Hello_World, len(Hello_World)


str = "Hello World"
Hello_World, length = unique_letters(str)
print(Hello_World,length)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




