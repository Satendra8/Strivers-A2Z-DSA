def fibonacci(n):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    i = 0
    curr = 1
    prev = 0
    while(i<n):
        print(prev, end = " ")
        temp = curr
        curr = prev + curr
        prev = temp
        
        i += 1

fibonacci(7) # 0 1 1 2 3 5 8

def fibonacci_recursice(n):
    """
    Time Complexity: O(2^n)
    Space Complexity: O(N) // functions waiting in stack
    """
    if n<=1:
        return n
        
    return fibonacci_recursice(n-1) + fibonacci_recursice(n-2)
    
for i in range(7+1):
    print(fibonacci_recursice(i), end = " ")


  
def fibonacci_using_generator(n):
    counter = 0
    curr = 1
    prev = 0
    while counter <= n:
        
        print(prev, end = " ")
        temp = curr
        curr = prev + curr
        prev = temp
        yield
        counter += 1
        
gt = fibonacci_using_generator(7)
next(gt)
next(gt)
next(gt)
next(gt)
next(gt)
next(gt)
next(gt)
next(gt)
next(gt)

