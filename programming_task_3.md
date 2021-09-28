[HL]  Programming Task 3: Create a file in your repository with name programming_task_3.md and include the solution to the problem below:
Using the program you created in Task 2, create a program that searches automatically for strange numbers. Can you find a number that will take 10 steps or more? 

num=int(input())
str(num)
from functools import reduce
from operator import mul
until steps<10:
def persistence(num, count=0):
    if num < 10:
        return count
new_num=reduce(mul,map(int, str(num)))
return persistence(new_num, count+1)
