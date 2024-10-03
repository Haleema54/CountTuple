'''

7) Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
program:
# Input: Read the tuple values as a single line of space-separated integers
tuple_values = tuple(map(int, input().split()))

# Input: Read the value to count
x = int(input())

# Count the occurrences of x in the tuple
count_x = tuple_values.count(x)

# Output: Print the count of occurrences
print(count_x)
'''
