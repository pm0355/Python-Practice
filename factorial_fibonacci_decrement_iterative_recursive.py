

#/**********************************************************************/ 

#/* CSC 280 - HW #9

#/* */ 

#/* modifier: Paul Mattioli

#/* */ 

#/* filename:  factorial_fibonacci_decrement_iterative_recursive.py

#/* modified from: laptop

#/* date last modified: 12/9

#/* */ 

#/**********************************************************************/
' the iterative factorial function here takes an integer, and mutliplies the product by i +1 and then returns the product' 
def factorialiterative(number):
    product = 1
    for i in range(number):
        product = product * (i+1)
    return product
    
'the recursive factorial function takes the base case and returns 1.For every other value returns the function(n-1)n'        
def factorialrecursive(number):
    if number == 0:
        return 1
    else:
        return (factorialrecursive(number-1)) * number 
' the decrement function takes a number greater than 0, enters a while loop that subtracts one from n and prints n until n is zero and then returns.'    
def decrement(n):
    if n > 0:
        print n
        while n > 0:
            n-=1
            print n
            if n <= 0:
                return 'Great'
    else:
        return 'Great'
'the recursive decrement function takes a number n and returns the function(n-1) until the base case n==0 which returns "great"'
def rdecrement(n):
    if n == 0:
        print 0
        return 'Great'
    else:
        print n 
        return rdecrement(n-1)
'the fibonacci funtion takes a list and appends an incremented i to the list until i = n'       
def fibonacci(n):
    fs = [0,1]
    i = 2
    while i <= n:
        fs.append(fs[i-1] + fs[i-2])
        i = i +1
    return fs
' the recursion fibonacci returns the sum of functions with (n-2) and (n-1), until the base case'
def recursionfibonacci(n):
    if (n == 0 or n == 1):
        return n
    else:
        return (recursionfibonacci(n-2) + recursionfibonacci(n-1))
' the printstring function returns the string until n = 0'
def printstring(STR, n):
    while n > 0:
        print STR
        n-=1
' recursive printstring prints the str and returns the function with n-1 until n ==0'
def recursiveprintstring(STR, n):
    if n == 0:
        return 
    else:
        print STR
        return recursiveprintstring(STR, n-1)
'the main calls each function and assigns them to a variable.the decrement functions worked outside of the main but for whatever reason would not print "great" so i added the print call.'
def main():
    
    a = factorialiterative(10)
    print 'iterative factorial: '+str(a)
   
    b = factorialrecursive(10)
    print 'recursive factorial: '+str(b)
    c = decrement(10)
    print 'iterative decrement: '+str(c)

    
    d = rdecrement(10)
    print 'recursive decrement:'+str(d)

    
    e = fibonacci(10)
    print 'iterative fibonacci:'+str(e)
    print e

    f = recursionfibonacci(10)
    print 'recursive fibonacci:'+str(f)
    
    print 'iterative PrintString:'
    g = printstring("I Love CS", 10)
    
    print 'recursive PrintString:'
    h = recursiveprintstring("I Love CS", 10)
    
main()
    

    
    
    
         
    

        
        

        

    
        
        
    
