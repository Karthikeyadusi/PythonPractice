#fibonacci using recursion

def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

def calculate_fib_terms(): 
    terms = int(input("Enter how many terms: "))
    print(f"Fibonacci series is: ", end=" ")
    for i in range(0,terms,1):
        print(fib(i), end=" ")


def calculate_fib_term():
    term = int(input("Enter which fibonacci term you want: "))
    print(f"Term {term} in fibonacci series is:  {fib(term)}")  
    

def switch_case(choice):
    switch = {
        "1" : calculate_fib_terms,
        "2" : calculate_fib_term
    }
    if choice in switch:
        switch[choice]()
    else:
        print("Invalid choice")

print("1.calculate complete fibonacci series, 2.find particular fibonacci term")
choice = input("Enter which one would you use: ")
switch_case(choice)