# 0x01. Python - if/else, loops, functions

## `0-positive_or_negative.py`
This program will assign a random signed number to the variable  `number`  each time it is executed. 
```
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$ 
```

## `1-last_digit.py`
This program will assign a random signed number to the variable   `number`  between `-10000 and 10000` each time it is executed.

-   The output of the program should be:
  
```
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ 
```
## `2-print_alphabet.py`
program prints the ASCII alphabet, in lowercase, not followed by a new line.
```
guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
```

## `3-print_alphabt.py`
a program prints the ASCII alphabet, in lowercase, not followed by a new line.

-   Print all the letters except  `q`  and  `e`
```
guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
```
## 4-print_hexa.py`
program prints all numbers from  `0`  to  `98`  in decimal and in hexadecimal (as in the following example)
```
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$
```
## `5-print_comb2.py`
Write a program that prints numbers from  `0`  to  `99`.

-   Numbers must be separated by  `,`, followed by a space
-   Numbers should be printed in ascending order, with two digits
-   The last number should be followed by a new line
```
guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x01$ 
```

## `6-print_comb3.py`
program that prints all possible different combinations of two digits.

-   Numbers separated by  `,`, followed by a space
-   The two digits which are different
-   `01`  and  `10`  are considered the same combination of the two digits  `0`  and  `1`
-   Print only the smallest combination of two digits
-   Numbers should be printed in ascending order, with two digits
-   The last number should be followed by a new line
```
guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x01$ 
```
## `7-islower.py`
`def islower(c):` function that checks for lowercase character.
-   Returns  `True`  if  `c`  is lowercase
-   Returns  `False`  otherwise
` 7-main.py ` used to run the function
```
guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
guillaume@ubuntu:~/0x01$ 
```
##  `8-uppercase.py`
`def uppercase(str):` function that prints a string in uppercase followed by a new line.
`8-main.py` used to run code
```
guillaume@ubuntu:~/0x01$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
guillaume@ubuntu:~/0x01$ 
```
## `9-print_last_digit.py`
`def print_last_digit(number):` a function that prints the last digit of a number.
`9-main.py` used to run this file
```
guillaume@ubuntu:~/0x01$ ./9-main.py
8044
guillaume@ubuntu:~/0x01$ 
```
## `10-add.py`
`def add(a, b):` a function that adds two integers and returns the result.
`10-main.py` used to run file
```
guillaume@ubuntu:~/0x01$ ./10-main.py
3
98
98
guillaume@ubuntu:~/0x01$ 
```
## `11-pow.py`
 `def pow(a, b):` a function that computes  `a`  to the power of  `b`  and return the value.
`11-main.py` used to run file
```
guillaume@ubuntu:~/0x01$ ./11-main.py
4
9604
1
0.0001
-1024
guillaume@ubuntu:~/0x01$ 
```
## `12-fizzbuzz.py`
`def fizzbuzz():` a function that prints the numbers from 1 to 100 separated by a space.
-   For multiples of three print  `Fizz`  instead of the number and for multiples of five print  `Buzz`.
-   For numbers which are multiples of both three and five print  `FizzBuzz`.
-   Each element should be followed by a space
`12-main.py` used to run file
```
guillaume@ubuntu:~/0x01$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
guillaume@ubuntu:~/0x01$ 
```
## `13-insert_number.c, lists.h`
**Technical interview preparation**:
`listint_t *insert_node(listint_t **head, int number);` a function in C that inserts a number into a sorted singly linked list.
-   Return: the address of the new node, or  `NULL`  if it failed

`lists.h` , `linked_lists.c`, `13-main.c` used to run file
```
carrie@ubuntu:0x01$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
carrie@ubuntu:0x01$ ./insert
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
27
98
402
1024
carrie@ubuntu:0x01$  
```

## `100-print_tebahpla.py` 
a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z`  in lowercase and  `Y`  in uppercase) , not followed by a new line.
```
guillaume@ubuntu:~/0x01$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbAguillaume@ubuntu:~/0x01$
```
## `101-remove_char_at.py`
 `def remove_char_at(str, n):` function that creates a copy of the string, removing the character at the position  `n`  (not the Python way, the “C array index”).
 `101-main.py` use to run file
```
guillaume@ubuntu:~/0x01$ ./101-main.py
Bes School
Chcago
 is fun!
School
Python
guillaume@ubuntu:~/0x01$ 
```

##  `102-magic_calculation.py`
Write the Python function  `def magic_calculation(a, b, c):`  that does exactly the same as the following Python bytecode:

```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```



> Written with [StackEdit](https://stackedit.io/).
