#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

def GameRes(computer,player):
    computer=computer.lower()
    player=player.lower()
    if computer==player:
        return None
    
    elif computer=='s':
        if player=='w':
            return False
        else:
            return True
        
    elif computer=='w':
        if player=='s':
            return True
        else:
            return False
    
    elif computer=='g':
        if player=='s':
            return False
        else:
            return True

print("Let's Play Snake Water Gun Game!")
print('Your Turn: Choose Snake(s), Water(w), Gun(g):')
player=input()

compRand=random.randint(1,3)
if compRand==1:
    computer='s'
elif compRand==2:
    computer='w'
else:
    computer='g'
    
print('Computer Turn: Choose Snake(s), Water(w), Gun(g): {}'.format(computer))

res=GameRes(computer,player)
if res==None:
    print('Match Tie!')
elif res==True:
    print('You Win!')
else:
    print('Better Luck Next Time!')

