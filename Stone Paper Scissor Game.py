#!/usr/bin/env python
# coding: utf-8

# In[20]:


import random

def GameRes(computer,player):
    computer=computer.lower()
    player=player.lower()
    if computer==player:
        return None
    
    elif computer=='s':
        if player=='sc':
            return False
        else:
            return True
        
    elif computer=='p':
        if player=='sc':
            return True
        else:
            return False
    
    elif computer=='sc':
        if player=='p':
            return False
        else:
            return True

print("Let's Play Stone Paper Scissor Game!")
print('Your Turn: Choose Stone(s), Paper(p), Scissor(sc):')
player=input()

compRand=random.randint(1,3)
if compRand==1:
    computer='s'
elif compRand==2:
    computer='p'
else:
    computer='sc'
    
print('Computer Turn: Choose Stone(s), Paper(p), Scissor(sc): {}'.format(computer))

res=GameRes(computer,player)

if res==None:
    print('Match Tie!')
elif res==True:
    print('You Win!')
else:
    print('Better Luck Next Time!')

