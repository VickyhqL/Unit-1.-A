# <!-- Programming Task 1: Create a file in your repository with name programming_task_1.md and include the solution to the problem below:
# Ask the user for  2 numbers, A and B, Output TRUE if one of them is 10 or if their sum is 10.
# Examples
# Makes10(9, 10) → TRUE
# Makes10(9, 9) → FALSE
# Makes10(1, 9) → TRUE -->

a=int(input())
b=int(input())
if a+b==10 or a==10 or b==10:
  print("TRUE")
else:
  print("FALSE")
