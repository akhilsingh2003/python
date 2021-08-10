# seed():seed intializes the random such that if we run it anywhere else and 
# as we want if the passed integer is same we will get same random value every time

import random 
random.seed(12)
print(random.random())