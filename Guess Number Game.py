#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random

print('Let\'s Find the Right Number')
print()

randomNumber = random.randint(1,101)
playerGuess = int(input('Enter your Guess: '))

userGuess = 1
if randomNumber == playerGuess:
    pass
else:
    while (randomNumber != playerGuess):
        if randomNumber == playerGuess:
            print('Whoaa! You guess it Right')
        else:
            print('OOPS! You guess it Wrong')
            print('Try Again!')
            if randomNumber > playerGuess:
                print('Number is GREATER than your Entered Guess')
            else:
                print('Number is SMALLER than your Entered Guess')

            playerGuess=int(input('Enter your Guess: '))
            userGuess+=1
        print()
        
print('Whoaa! You guess it Right')
if userGuess==1:
    print('You Took only 1 Guess.')
else:
    print('You Took {} Guesses'.format(userGuess))


# In[ ]:




