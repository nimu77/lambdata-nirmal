# classwork
# my_lambdata.my_mod_two.py
import pandas as pd

# pdb; pdb.set_trace()

def add_state_names_column(my_df):
    """
    Add a column of corresponding state names to a dataframe.

    Params (my_df) a DataFrame with a column called "abbrev"
    that has state abbreviation.

    Return a copy of a original DataFrame, but return a copy with a
    extra column.
    """
    new_df = my_df.copy()

    names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn", "TX": "Texas"}

    new_df['names'] = new_df['abbrev'].map(names_map)

    return new_df

if __name__ == '__main__':

    df = pd.DataFrame({"abbrev": ["CA", "CO", "CT", "TX", "UT"]})

    print(df)

    corr_df = add_state_names_column(df)

    print(corr_df)
