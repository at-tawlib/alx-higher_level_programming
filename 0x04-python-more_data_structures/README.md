# 0x04. Python - More Data Structures: Set, Dictionary

## `0-square_matrix_simple.py`, `0-main.py`
has a function that computes the square value of all integers of a matrix.

-   Prototype:  `def square_matrix_simple(matrix=[]):`
-   `matrix`  is a 2 dimensional array
-   Returns a new matrix:
    -   Same size as  `matrix`
    -   Each value should be the square of the value of the input
```
guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 
```
##  `1-search_replace.py` ,  `1-main.py`
replaces all occurrences of an element by another in a new list.

-   Prototype:  `def search_replace(my_list, search, replace):`
-   `my_list`  is the initial list
-   `search`  is the element to replace in the list
-   `replace`  is the new element
```
guillaume@ubuntu:~/0x04$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/0x04$ 
```
##   `2-uniq_add.py`, `2-main.py`
Write a function that adds all unique integers in a list (only once for each integer).

-   Prototype:  `def uniq_add(my_list=[]):`
```
guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
guillaume@ubuntu:~/0x04$ 
```
## `3-common_elements.py` ,  `3-main.py`
returns a set of common elements in two sets.
-   Prototype:  `def common_elements(set_1, set_2):`
```
guillaume@ubuntu:~/0x04$ ./3-main.py
['C']
guillaume@ubuntu:~/0x04$ 
```
## `4-only_diff_elements.py` ,  `4-main.py`
returns a set of all elements present in only one set.
-   Prototype:  `def only_diff_elements(set_1, set_2):`
```
guillaume@ubuntu:~/0x04$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/0x04$ 
```
##  `5-number_keys.py` ,`5-main.py`
returns the number of keys in a dictionary.
-   Prototype:  `def number_keys(a_dictionary):`
```
guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$ 
```
## `6-print_sorted_dictionary.py` ,  `6-main.py`
prints a dictionary by ordered keys.
-   Prototype:  `def print_sorted_dictionary(a_dictionary):`
-   Keys should be sorted by alphabetic order
-   Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
```
guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/0x04$ 
```
##  `7-update_dictionary.py` , `7-main.py`
function that replaces or adds key/value in a dictionary.
-   Prototype:  `def update_dictionary(a_dictionary, key, value):`
-   If a key exists in the dictionary, the value will be replaced
-   If a key doesn’t exist in the dictionary, it will be created
```
guillaume@ubuntu:~/0x04$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/0x04$ 

```
##  `8-simple_delete.py` , `8-main.py`
function that deletes a key in a dictionary.
-   Prototype:  `def simple_delete(a_dictionary, key=""):`
-   If a key doesn’t exist, the dictionary won’t change
```
guillaume@ubuntu:~/0x04$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/0x04$ 

```
##  `9-multiply_by_2.py` , `9-main.py`
function that returns a new dictionary with all values multiplied by 2
-   Prototype:  `def multiply_by_2(a_dictionary):`
```
guillaume@ubuntu:~/0x04$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/0x04$ 
```
##   `10-best_score.py`  , `10-main.py`
function that returns a key with the biggest integer value.
-   Prototype:  `def best_score(a_dictionary):`
-   If no score found, return  `None`
```
guillaume@ubuntu:~/0x04$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/0x04$ 
```

## `11-multiply_list_map.py` ,  `11-main.py`
function that returns a list wih all values multiplied by a number without using any loops.

-   Prototype:  `def multiply_list_map(my_list=[], number=0):`
-   Returns a new list:
    -   Same length as  `my_list`
    -   Each value should be multiplied by  `number`
-   Initial list should not be modified
```
guillaume@ubuntu:~/0x04$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/0x04$ 
```

## `12-roman_to_int.py` , `12-main.py`
**Technical interview preparation**:
a function  `def roman_to_int(roman_string):`  that converts a  [Roman numeral](https://alx-intranet.hbtn.io/rltoken/oSuwqUrL0BL_hi4VqVvs_g "Roman numeral")  to an integer.

-   You can assume the number will be between 1 to 3999.
-   `def roman_to_int(roman_string)`  must return an integer
-   If the  `roman_string`  is not a string or  `None`, return 0
```
guillaume@ubuntu:~/0x04$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
guillaume@ubuntu:~/0x04$ 
```
## `100-weight_average.py` , `100-main.py`
function that returns the weighted average of all integers tuple  `(<score>, <weight>)`

-   Prototype:  `def weight_average(my_list=[]):`
-   Returns  `0`  if the list is empty
```
guillaume@ubuntu:~/0x04$ ./100-main.py
Average: 2.80
guillaume@ubuntu:~/0x04$ 
```
##  `101-square_matrix_map.py` , `101-main.py`
function that computes the square value of all integers of a matrix using  `map`
-   Prototype:  `def square_matrix_map(matrix=[]):`
-   `matrix`  is a 2 dimensional array
-   Returns a new matrix:
    -   Same size as  `matrix`
    -   Each value should be the square of the value of the input
-   Initial matrix should not be modified
```
guillaume@ubuntu:~/0x04$ ./101-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 
```

## `102-complex_delete.py` , `102-main.py`
function that deletes keys with a specific value in a dictionary.
-   Prototype:  `def complex_delete(a_dictionary, value):`
-   If the value doesn’t exist, the dictionary won’t change
-   All keys having the searched value have to be deleted
```
guillaume@ubuntu:~/0x04$ ./102-main.py
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
--
--
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
guillaume@ubuntu:~/0x04$ 
```

> Written with [StackEdit](https://stackedit.io/).t
