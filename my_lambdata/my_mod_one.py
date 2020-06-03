import pandas as pd


def checks_null(a):
    '''checks to see if dataframe has null values'''
    a = pd.DataFrame(a)

    if a.isnull().values.any():
        print(f'DataFrame has some null values, please replace it or drop it.')
    else:
        print(f'DataFrame is good to go. No null values.')


if __name__ == '__main__':
    y = pd.DataFrame(value)
    print(checks(y))
