#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calulate_effective_rate(i,m):
    return (1+i/m)**m-1
stated_rate = float(input("What is the nominal return : "))
number_of_compounding_periods = int(input("What is the number of compounding periods : "))
effective_rate = calulate_effective_rate(stated_rate,number_of_compounding_periods)
print("The effective rate is {}, the nominal rate is {}".format(round(effective_rate,4)*100,stated_rate*100))
input()


# In[ ]:



