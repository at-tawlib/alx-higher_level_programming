# 0x12. JavaScript - Warm up

## [0-javascript_is_amazing.js](0-javascript_is_amazing.js)
script that prints “JavaScript is amazing”:
```
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
```

## [1-multi_languages.js](1-multi_languages.js)
a script that prints 3 lines:
-   The first line: “C is fun”
-   The second line: “Python is cool”
-   The third line: “JavaScript is amazing”
```
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
```

## [2-arguments.js](2-arguments.js)
script that prints a message depending of the number of arguments passed:
-   If no arguments are passed to the script, print “No argument”
-   If only one argument is passed to the script, print “Argument found”
-   Otherwise, print “Arguments found”
Reference:  [process.argv](https://intranet.alxswe.com/rltoken/5kTYi3rxb6KM1_pivm-tXg "process.argv")
```
guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$ 
```
## [3-value_argument.js](3-value_argument.js)
script that prints the first argument passed to it:
-   If no arguments are passed to the script, print “No argument”
-   You are not allowed to use  `length`
```
guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$ 
```

## [4-concat.js](4-concat.js)
script that prints two arguments passed to it, in the following format: “  is  ”
```
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
```
## [5-to_integer.js](5-to_integer.js)
script that prints  `My number: <first argument converted in integer>`  if the first argument can be converted to an integer:
-   If the argument can’t be converted to an integer, print “Not a number”
```
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$
