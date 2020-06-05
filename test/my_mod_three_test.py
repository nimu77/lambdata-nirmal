# write some code using unittest to test our enlarge() function works as desinfed


import unittest
import pandas as pd
from my_lambdata.my_mod_three import add_columns


class TestModThree(unittest.TestCase):

    def test_add_columns(self):
        df = pd.DataFrame({"Date": ['20180206', '20190307',
                                    '20150621', '20191222']})

        self.assertEqual(len(df.columns), 1)
        self.assertEqual(df.iloc[0]['Date'], '20180206')

        corr_df = add_columns(df)

        self.assertEqual(len(corr_df.columns), 4)
        self.assertEqual(corr_df.iloc[0]['Years'], 2018)




if __name__ == '__main__':
    unittest.main()
