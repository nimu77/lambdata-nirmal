
import pandas as pd


def enlarge(n):
    """
    Param n is a number

    Function will enlarge the number
    """
    return n * 100


# y =  int(input("Please choose a number"))
# print(y, enlarge(y))

if __name__ == '__main__':
    y = int(input("Please choose a number"))
    print(y, enlarge(y))
