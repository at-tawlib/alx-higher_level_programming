# 0x08. Python - More Classes and Objects

## [0-rectangle.py](0-rectangle.py), [0-main.py](0-main.py)

has an empty class  `Rectangle`  that defines a rectangle
```
guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/0x08$ 
```

## [1-rectangle.py](1-rectangle.py), [1-main.py](1-main.py)
add private variables (height and weight) to the rectangle

```
guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 
```

## [2-rectangle.py](2-rectangle.py), [2-main.py](2-main.py)
add functions to calculate area and perimeter of the rectangle
```
guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 
```

## [3-rectangle.py](3-rectangle.py), [3-main.py](3-main.py)

add `print()` and `str()` for the rectangle
```
guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/0x08$ 
```
##  [4-rectangle.py](4-rectangle.py), [4-main.py](4-main.py)
add `repr()`  function to the class
```
guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$ 
```
## [5-rectangle.py](5-rectangle.py), [5-main.py](5-main.py)


-   Print the message  `Bye rectangle...`  (`...`  being 3 dots not ellipsis) when an instance of  `Rectangle`  is deleted
```
guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/0x08$ 
```

## [6-rectangle.py](6-rectangle.py), [6-main.py](6-main.py)
-   Public class attribute  `number_of_instances`:
    -   Initialized to  `0`
    -   Incremented during each new instance instantiation
    -   Decremented during each instance deletion
```
guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/0x08$ 
```
## [7-rectangle.py](7-rectangle.py), [7-main.py](7-main.py)
-   Public class attribute  `print_symbol`:
    -   Initialized to  `#`
    -   Used as symbol for string representation
    -   Can be any type
```
guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
```

## [8-rectangle.py](8-rectangle.py), [8-main.py](8-mai.py)

-   Static method  `def bigger_or_equal(rect_1, rect_2):`  that returns the biggest rectangle based on the area
    -   `rect_1`  must be an instance of  `Rectangle`, otherwise raise a  `TypeError`  exception with the message  `rect_1 must be an instance of Rectangle`  
        
    -   `rect_2`  must be an instance of  `Rectangle`, otherwise raise a  `TypeError`  exception with the message  `rect_2 must be an instance of Rectangle`  
        
    -   Returns  `rect_1`  if both have the same area value
```
guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 

```

## [9-rectangle.py](9-rectangle.py), [9-main.py](9-main.py)
-   Class method  `def square(cls, size=0):`  that returns a new Rectangle instance with  `width == height == size`
```
guillaume@ubuntu:~/0x08$ ./9-main.py
Area: 25- Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
```

## [101-nqueens.py](101-nqueens.py)
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. 
this program that solves the N queens problem.

-   Usage:  `nqueens N`
    -   If the user called the program with the wrong number of arguments, print  `Usage: nqueens N`, followed by a new line, and exit with the status  `1`
-   where N must be an integer greater or equal to  `4`
    -   If N is not an integer, print  `N must be a number`, followed by a new line, and exit with the status  `1`
    -   If N is smaller than  `4`, print  `N must be at least 4`, followed by a new line, and exit with the status  `1`
-   The program  prints every possible solution to the problem
    -   One solution per line
    -   Format: see example

Read:  [Queen](https://alx-intranet.hbtn.io/rltoken/dAQmi8RxMnLH-iHBzkz-lw "Queen"),  [Backtracking](https://alx-intranet.hbtn.io/rltoken/TGXZXdY2Awg8m4mSjlrjjA "Backtracking")

```
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
```
> Written with [StackEdit](https://stackedit.io/). 
