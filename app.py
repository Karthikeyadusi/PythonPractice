#print("Hello, World")

#celsius -> fahrenheit

#Write a program to convert temperature from Celsius to Fahrenheit. Input temperature in Celsius as a float, output the Fahrenheit value.
'''celsius = float(input("Enter temperature in celsius: "))
fahrenheit = ((9/5)*celsius) + 32
print("Temperature in fahrenheit is: ", fahrenheit)
'''

#Create a program that asks for two numbers and prints their sum.

'''a = int(input("Enter no1: "))
b = int(input("Enter no2: "))
print("Their sum is : ",a+b)'''


#Write a program that takes two integers and returns True if one is a multiple of the other.

'''a = int(input("enter no1: "))
b = int(input("enter no2: "))

if a%b==0 or b%a==0:
    print("True")
else:
    print("False")'''

#Write a program to check if a given string is a palindrome.

'''string = input("Enter a string : ")

reversed_string = string[::-1]

if reversed_string == string:
    print("its a palindrome")
else:
    print("not a palindrome")'''


#number to word converter

'''num = input("Enter number: ")
num_to_word = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}
for i in num:
    word = num_to_word.get(i)
    print(word, end=" ")
'''


#emoji converter
'''
sen = input(">")
words = sen.split(" ")
word_to_emoji = {
    ":)" : "😃",
    ":(" : "😟",
}
new_sen = ""
for i in words:
    new_sen += word_to_emoji.get(i,i) + " "
print(new_sen)
'''
#emoji converter using functions
'''def emoji_converter(sen):
    word = sen.split(" ")
    word_to_emoji = {
        ":)" : "😃",
        ":(" : "😟"
    }
    new_sen = ""
    for i in word:
        new_sen  += word_to_emoji.get(i,i) + " "
    return new_sen
sen = input("Enter message: ")
print(emoji_converter(sen))'''

#Greeting Function
'''
def greet_user(name):
    print(f"Hello, {name}")

greet_user("Karthik")'''

#Sum of List
'''
def sum_of_list(list):
    sum = 0
    for i in list:
        sum += i
    print(f"The sum of the items in list is : {sum}")

sum_of_list([1,2,3,4])'''

#factorial of a number
'''
def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(f"Factorial of 4 is : {factorial(4)}")'''


#fibonacci series
'''
def fibonacci(num):
    print("Fibonacci Series:")
    a,b=0,1
    for i in range(0,num,1):
        print(a, end=" ")
        next = a+b
        a=b
        b=next


terms = int(input("Enter how many terms: "))
fibonacci(terms)
'''
        

#fibonacci using recursion
'''
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

      
'''




#count vowels in a string



