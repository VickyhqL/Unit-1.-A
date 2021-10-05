# [HL]  Programming Task 2: Create a file in your repository with name programming_task_2.md and include the solution to the problem below:
# Strange Numbers: Given a number as a String N. Multiply all of its digits, and repeat the same with the product obtained till the product consists of only one digit. Output the number of steps taken to do so. 
# Example: N = 39
# Step 1: 3 * 9 = 27
# Step 2: 2 * 7 = 14
# Step 3: 1 * 4 = 4
# Since it took us 3 steps to reach a number with only 1 digit, the output is 3.

num=int(input())
from functools import reduce
from operator import mul
def persistence(num, count=0):
    if num < 10:
        return count
new_num=reduce(mul,map(int, str(num)))
return persistence(new_num, count+1)
