# lambdata-nirmal

## This is where I would upload packages for python

## Installation
```sh
pip install -i https://test.pypi.org/simple/ lambdata-nirmal==1.7
```



## Usage

### enlarges input by 100.
```py
from my_lambdata.my_mod import enlarge
print(enlarge(10))
```

### function to check dataframe for nulls.
```py
from my_lambdata.my_mod_one import checks_null
checks_null(df)
```

### function that adds a column with full names for countries if abbreviated
```py
from my_lambdata.my_mod_two import add_state_names_column
add_state_names_column()
```

### function that adds three new columns to a
### dataframe after converting a column to a datetime
### format
```py
from my_lambdata.my_mod_three import return_year_month_date_columns
return_year_month_date_columns()
```

### class
```sh
class DateTime():
  attributes: year
              month
              date
              hour
              minute
              seconds
  methods: timeline()
```
