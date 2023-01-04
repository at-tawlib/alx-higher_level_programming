# 0x07. Python - Test-driven development

## [0-add_integer.py](0-add_integer.py), [0-main.py](0-main.py), [tests/0-add_integer.txt](tests/0-add_integer.txt)
```add_integer(a, b=98):``` function that adds 2 integers.
```
guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/0x07$ 
```

## [2-matrix_divided.py](2-matrix_divided.py),  [2-main.py](2-main.py),  [tests/2-matrix_divided.txt](tests/2-matrix_divided.txt)

has a function that divides all elements of a matrix.
```
guillaume@ubuntu:~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
```
## [3-say_my_name.py](3-say_my_name.py),  [3-main.py](3-main.py), [tests/3-say_my_name.txt](tests/3-say_my_name.txt)
has a function that prints  `My name is <first name> <last name>`
```
guillaume@ubuntu:~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
```

##  [4-print_square.py](4-print_square.py), [4-main.py](4-main.py),  [tests/4-print_square.txt](tests/4-print_square.txt)
has a function that prints a square with the character  `#`.
```
guillaume@ubuntu:~/0x07$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########

#

size must be >= 0

guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
guillaume@ubuntu:~/0x07$ 
```

## [5-text_indentation.py](5-text_indentation.py),   [5-main.py](5-main.py), [tests/5-text_indentation.txt](tests/5-text_indentation.txt)

has a function that prints a text with 2 new lines after each of these characters:  `.`,  `?`  and  `:`
```
guillaume@ubuntu:~/0x07$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/0x07$ 
```
## [tests/6-max_integer_test.py](tests/6-max_integer_test.py), [6-max_integer.py](6-max_integer.py), [6-main.py](6-main.py)

unittests for the function  `def max_integer(list=[]):`.
```
guillaume@ubuntu:~/0x07$ ./6-main.py
4
4
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/0x07$ 
```
## [100-matrix_mul.py](100-matrix_mul.py),  [tests/100-matrix_mul.txt](tests/100-matrix_mul.txt), [100-main.py](100-main.py)
function that multiplies 2 matrices:

-   Read:  [Matrix multiplication - only Matrix product (two matrices)](https://alx-intranet.hbtn.io/rltoken/Qw_rYR3lYYL5DHDH-iCWCA "Matrix multiplication - only Matrix product (two matrices)")
    
```
guillaume@ubuntu:~/0x07$ ./100-main.py 
[[7, 10], [15, 22]]
[[13, 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
```

## [101-lazy_matrix_mul.py](101-lazy_matrix_mul.py), [tests/101-lazy_matrix_mul.txt](tests/101-lazy_matrix_mul.txt), [101-main.py](101-main.py)
function that multiplies 2 matrices by using the module  [NumPy](https://alx-intranet.hbtn.io/rltoken/sXnBuOVSyhKEGt-biOyOWg "NumPy")

To install it:  `pip3 install numpy==1.15.0`

```
guillaume@ubuntu:~/0x07$ ./101-main.py 
[[ 7 10]
 [15 22]]
[[13 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 
guillaume@ubuntu:~/0x07$ 
```

## [102-python.c](102-python.c), [102-tests.py](102-tests.py)
function prints Python strings.
-   Format: see example
-   If  `p`  is not a valid string, print an error message (see example)
-   Read:  [Unicode HOWTO](https://alx-intranet.hbtn.io/rltoken/UkkHHaILiYf9d_a3nc4Bxw "Unicode HOWTO")

About:

-   Python version: 3.4
-   shared library will be compiled with this command line:  `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`

```
julien@ubuntu:~/0x07. Pyhton Strings$ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
julien@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n'existe pas
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない
[.] string object info
  [ERROR] Invalid String Object
julien@ubuntu:~/0x07. Pyhton Strings$ 
```

> Written with [StackEdit](https://stackedit.io/).
