#!/usr/bin/env python3

def greet_programmer():
    """Prints 'Hello, programmer!'"""
    print("Hello, programmer!")

def greet(name):
    """Prints 'Hello, {name}!'"""
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """Prints 'Hello, {name}!', defaults to 'programmer' if no argument is provided."""
    print(f"Hello, {name}!")

def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def halve(number):
    """Returns half of the given number."""
    if not isinstance(number, (int, float)):
        return None
    return number / 2
