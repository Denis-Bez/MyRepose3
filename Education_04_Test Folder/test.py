import re

from config import IYUTEER
import matplotlib.pyplot as plt
import pandas as pd














# Delite simbols in text
""" def main():
    a = ["     https://pythonstart.ru/string/strip-python", "fo  o", "bar      ", "bas"]

    a = [i.strip() for i in a]
    print(a) """

# Try Except
""" def main():
    a = 'Yohoo!'
    list = ['car', 1, 'feef', 'foo', 'bar', 'bas']

    try:
        a = list[6]
    except Exception as e:
	    print(e)
    finally:
	    print(a) """


# Decorators
""" def decorator (func):

    def inner():
        print('start decorator...')
        func()
        print('finish decorator...')
    
    return inner

def say():    
    print('Hello, Hell')

def main():
    say = 0
    say = decorator(say)
    print(say) """
    
    
if __name__ == "__main__":
    main()

