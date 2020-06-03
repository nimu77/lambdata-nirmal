import pandas as pd


def return_year_month_date_columns(my_df):
    '''
    Adds three columns to a dataframe.

    Params (my_df) a DataFrame with a column called "Date".

    Returns a copy of original dataframe, but with three extra columns.
    Years, Months and DD.
    '''

    new_df = my_df.copy()

    new_df['Date'] = pd.to_datetime(new_df['Date'])

    new_df['Years'] = new_df['Date'].dt.year

    new_df['Months'] = new_df['Date'].dt.month

    new_df['DD'] = new_df['Date'].dt.day

    return new_df


if __name__ == '__main__':

    df = pd.DataFrame({"Date": ['20180206', '20190307',
                                '20150621', '20191222']})

    print(df)

    corr_df = return_year_month_date_columns(df)

    print(corr_df)
