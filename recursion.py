# The following program is the solution to the Recursion Practice quiz of the Data Structures & Algorithms class by Grow with Google/Udacity

def get_fib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    else:
        ans = get_fib(position-1) + get_fib(position-2)
        return ans

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
