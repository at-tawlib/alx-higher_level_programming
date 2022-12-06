# 0x03. Python - Data Structures: Lists, Tuples
## `0-print_list_integer.py`, `0-main.py`
has a function `def print_list_integer(my_list=[]):` that prints all integers of a list.
```
guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```
## `1-element_at.py`, `1-main.py`
has a function `def element_at(my_list, idx)` that retrieves an element from a list like in C.
-   If  `idx`  is negative, the function should return  `None`
-   If  `idx`  is out of range (> of number of element in  `my_list`), the function should return  `None`
```
guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
```
## `2-replace_in_list.py`,  `2-main.py`
has a function, `def replace_in_list(my_list, idx, element)` that replaces an element of a list at a specific position (like in C).
-   If  `idx`  is negative, the function should not modify anything, and returns the original list
-   If  `idx`  is out of range (> of number of element in  `my_list`), the function should not modify anything, and returns the original list
```
guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
```
##  `3-print_reversed_list_integer.py`,   `3-main.py`
has a function `def print_reversed_list_integer(my_list=[])` that prints all integers of a list, in reverse order.
```
guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
```
##   `4-new_in_list.py`, `4-main.py`
has a function that replaces an element in a list at a specific position without modifying the original list (like in C).
-   If  `idx`  is negative, the function should return a copy of the original  `list`
-   If  `idx`  is out of range (> of number of element in  `my_list`), the function should return a copy of the original  `list`
```
guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
```
## `5-no_c.py`, `5-main.py`
has a function that removes all characters  `c`  and  `C`  from a string without using  `str.replace()`

```
guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
```
## `6-print_matrix_integer.py`,   `6-main.py`
has a function that prints a matrix of integers.
```
guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```


##  `7-add_tuple.py`, `7-main.py`
has a function that adds 2 tuples.
-   Returns a tuple with 2 integers:
    -   The first element should be the addition of the first element of each argument
    -   The second element should be the addition of the second element of each argument
-   If a tuple is smaller than 2, use the value  `0`  for each missing integer
-   If a tuple is bigger than 2, use only the first 2 integers

```
guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
```
##  `8-multiple_returns.py`, `8-main.py`
has a function that returns a tuple with the length of a string and its first character.
-   If the sentence is empty, the first character should be equal to  `None`
```
guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/0x03$ 
```
##  `9-max_integer.py`,`9-main.py`
has  a function that finds the biggest integer of a list.
-   If the list is empty, return  `None`
```
guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$ 
```
##  `10-divisible_by_2.py`,  `10-main.py`
has a function that finds all multiples of 2 in a list.
-   Return a new list with  `True`  or  `False`, depending on whether the integer at the same position in the original list is a multiple of 2
-   The new list should have the same size as the original list
-   You are not allowed to import any module
```
guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$ 
```
##  `11-delete_at.py`, `11-main.py`
has a function that deletes the item at a specific position in a list.
-   If  `idx`  is negative or ou of range, nothing change (returns the same list)
```
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$ 
```
## `12-switch.py`,
switches value of  `a`  and  `b`
```
guillaume@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/0x03$ 
```
## `13-is_palindrome.c, lists.h`
**Technical interview preparation**:
has a function in C that checks if a singly linked list is a palindrome.
-   Return:  `0`  if it is not a palindrome,  `1`  if it is a palindrome
-   An empty list is considered a palindrome
```
carrie@ubuntu:0x03$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
carrie@ubuntu:0x03$ ./palindrome
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
carrie@ubuntu:0x03$
```

> Written with [StackEdit](https://stackedit.io/).t
