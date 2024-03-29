# 0x13. JavaScript - Objects, Scopes and Closures
## [0-rectangle.js](0-rectangle.js) , [0-main.js](0-main.js)
has an empty class  `Rectangle`  that defines a rectangle:
```
guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 
```

## [1-rectangle.js](1-rectangle.js) , [1-main.js](1-main.js)
a class  `Rectangle`  that defines a rectangle:
-   The constructor must take 2 arguments  `w`  and  `h`
-   Initialize the instance attribute  `width`  with the value of  `w`
-   Initialize the instance attribute  `height`  with the value of  `h`
```
guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$ 
```
## [2-rectangle.js](2-rectangle.js) , [2-main.js](2-main.js)
a class  `Rectangle`  that defines a rectangle:
-   If  `w`  or  `h`  is equal to 0 or not a positive integer, create an empty object
```
guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$ 
```
## [3-rectangle.js](3-rectangle.js), [3-main.js](3-main.js)
a class  `Rectangle`  that defines a rectangle:
-   The constructor must take 2 arguments:  `w`  and  `h`
-   Create an instance method called  `print()`  that prints the rectangle using the character  `X`
```
guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$ 
```
## [4-rectangle.js](4-rectangle.js), [4-main.js](4-main.js)
class  `Rectangle`  that defines a rectangle:
-   Create an instance method called  `rotate()`  that exchanges the  `width`  and the  `height`  of the rectangle
-   Create an instance method called  `double()`  that multiples the  `width`  and the  `height`  of the rectangle by 2
```
guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$ 
```
## [5-square.js](5-square.js) , [5-main.js](5-main.js)
class  `Square`  that defines a square and inherits from  `Rectangle`  of  `4-rectangle.js`:
-   The constructor must take 1 argument:  `size`
```
guillaume@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
guillaume@ubuntu:~/0x13$ 
```
## [6-square.js](6-square.js) , [6-main.js](6-main.js)
class  `Square`  that defines a square and inherits from  `Square`  of  [5-square.js](5-square.js):
-   Create an instance method called  `charPrint(c)`  that prints the rectangle using the character  `c`
    -   If  `c`  is  `undefined`, use the character  `X`
```
guillaume@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
guillaume@ubuntu:~/0x13$ 
```
## [7-occurrences.js](7-occurrences.js) , [7-main.js](7-main.js)
has a function that returns the number of occurrences in a list:
```
guillaume@ubuntu:~/0x13$ ./7-main.js
1
4
2
guillaume@ubuntu:~/0x13$ 
```
## [8-esrever.js](8-esrever.js) , [8-main.js](8-main.js)
a function that returns the reversed version of a list:
```
guillaume@ubuntu:~/0x13$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'School' ]
guillaume@ubuntu:~/0x13$ 
```
## [9-logme.js](9-logme.js) , [9-main.js](9-main.js)
has a function that prints the number of arguments already printed and the new argument value. (see example below)
```
guillaume@ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Best
2: School
guillaume@ubuntu:~/0x13$ 
```
## [10-converter.js](10-converter.js) , [10-main.js](10-main.js)
function that converts a number from base 10 to another base passed as argument:
```
guillaume@ubuntu:~/0x13$ ./10-main.js
2
12
89
2
c
59
guillaume@ubuntu:~/0x13$ 
```
## [100-map.js](100-map.js) 
a script that imports an array and computes a new array.
-   import  `list`  from the file  [100-data.js](100-data.js)
-   You must use a  `map`.  [Tips](https://intranet.alxswe.com/rltoken/LOEW51ZbYDjO4KZCFevzNQ "Tips")
-   A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
-   Print both the initial list and the new list
```
guillaume@ubuntu:~/0x13$ ./100-map.js 
[ 1, 2, 3, 4, 5 ]
[ 0, 2, 6, 12, 20 ]
guillaume@ubuntu:~/0x13$ 
```
## [101-sorted.js](101-sorted.js)
script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
-   import  `dict`  from the file  [101-data.js](101-data.js)
-   In the new dictionary:
    -   A key is a number of occurrences
    -   A value is the list of user ids
-   Print the new dictionary at the end
```
guillaume@ubuntu:~/0x13$ ./101-sorted.js 
{ '1': [ '89', '91', '93' ], '2': [ '90', '94' ], '3': [ '92' ] }
guillaume@ubuntu:~/0x13$ 
```
## [102-concat.js](102-concat.js)
script that concats 2 files.
-   The first argument is the file path of the first source file
-   The second argument is the file path of the second source file
-   The third argument is the file path of the destination
```
guillaume@ubuntu:~/0x13$ cat fileA
C is fun!
guillaume@ubuntu:~/0x13$ cat fileB
Python is Cool!!!
guillaume@ubuntu:~/0x13$ ./102-concat.js fileA fileB fileC
guillaume@ubuntu:~/0x13$ cat fileC
C is fun!
Python is Cool!!!
guillaume@ubuntu:~/0x13$ 
```
> Written with [StackEdit](https://stackedit.io/).
