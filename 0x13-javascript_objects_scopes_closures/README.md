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


