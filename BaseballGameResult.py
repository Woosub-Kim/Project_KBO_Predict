#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 승1패 함수1
def result_fnc1(difference):
    if difference >= 2:
        return 'away'
    elif difference <= -2:
        return  'home'
    else:
        return 'near'
#승무패
def result_fnc0(difference):
    if difference >= 1:
        return 'away'
    elif difference <= -1:
        return  'home'
    else:
        return 'near'

