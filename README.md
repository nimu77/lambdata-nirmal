# lambdata-nirmal

## This is where I would upload packages for python

## Installation
```sh
pip install -i https://test.pypi.org/simple/ lambdata-nirmal==1.6
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
