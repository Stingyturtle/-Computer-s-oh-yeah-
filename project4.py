import random
#random.randint(1,6)
rollNum= 0
sixrolled=0
while sixrolled <1000:
   rolling=random.randint(1,6)
   rollNum = rollNum + 1
   if rolling==6:
       sixrolled=sixrolled+1

oddsofgettingasix= rollNum/1000
print('it takes ',oddsofgettingasix ,'rolls to get a six')

#change this, so that it stops as soon as it rolls a 6
#then count how many rolls it took to get to 6