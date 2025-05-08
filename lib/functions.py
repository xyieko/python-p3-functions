#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    

def greet(name):
    
    print(f"Hello, Guido!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("Guido")

def add(num1, num2):
    return 45 + 55 


    

def halve(x):
    if isinstance(x, (int, float)):  
        return x / 2
    else:
        return None

