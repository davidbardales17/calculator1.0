from functools import total_ordering
from ntpath import join
from operator import sub, truediv
from functools import reduce

#Initial Question to decide what math operation will be done
question1 = input("Do you want to add, subtract, multiply, or divide? ")

#Question to decide what numbers will be used
number_question = input("Plesase write down all the numbers: ")

numbers = number_question

#open list to place number from string question into integer form
list1 = []

#Use split method to place numbers into list
for number in numbers.split():
    list1.append(int(number))

numbers = list1

#Create functions to organize code plus help with scaleability
def add(numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)

def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    print(total)

# use functools.reduce paired with either operator.sub for subtraction or operator.truediv for division
def subtract(numbers):
    print(reduce(sub, numbers))

def divide(numbers):
    print(reduce(truediv, numbers))

#If state to decide what function will be excecuted
if question1 == "add":
    add(numbers)
elif question1 == "multiply":
    multiply(numbers)
elif question1 == "subtract":
    subtract(numbers)
elif question1 == "divide":
    divide(numbers)
else:
    print("Error type 'add' 'subtract' 'multiply' or 'divide'")








