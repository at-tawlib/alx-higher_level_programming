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
```

## [6-multi_languages_loop.js](6-multi_languages_loop.js)
script that prints 3 lines: (like  [1-multi_languages.js](1-multi_languages.js)) but by using an array of string and a loop
```
guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
```
## [7-multi_c.js](7-multi_c.js)
script that prints  `x`  times “C is fun”
-   Where  `x`  is the first argument of the script
-   If the first argument can’t be converted to an integer, print “Missing number of occurrences”
```
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
```
## [8-square.js](8-square.js)
script that prints a square using the `X` character
-   The first argument is the size of the square
```
guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
```
## [9-add.js](9-add.js)
script that prints the addition of 2 integers using a function
-   The first argument is the first integer
-   The second argument is the second integer
```
guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
```

## [10-factorial.js](10-factorial.js)
script that computes and prints a factorial
-   The first argument is integer (argument can be cast as integer) used for computing the factorial
-   Factorial of  `NaN`  is  `1`
```
guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
```
## [11-second_biggest.js](11-second_biggest.js)
script that searches the second biggest integer in the list of arguments.
-   You can assume all arguments can be converted to integer
-   If no argument passed, print  `0`
-   If the number of arguments is 1, print  `0`
```
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
```
## [12-object.js](12-object.js)
Update this script to replace the value  `12`  with  `89`:
```
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
```
## [13-add.js](13-add.js), [13-main.js](13-main.js)
has a function that returns the addition of 2 integers.
-   The function must be visible from outside
[Tip](https://intranet.alxswe.com/rltoken/1k6VPdLchwtGubOfPyGL1Q "Tip")
```
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
```
## [100-let_me_const.js](100-let_me_const.js), [100-main.js](100-main.js)
modifies the value of  `myVar`  to  `333`
```
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
```

## [101-call_me_moby.js](101-call_me_moby.js), [101-main.js](101-main.js)
has a function that executes  `x`  times a function.
-   The function must be visible from outside
```
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ 
```
## [102-add_me_maybe.js](102-add_me_maybe.js) , [102-main.js](102-main.js)
a function that increments and calls a function.
-   The function must be visible from outside
```
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$ 
```
## [103-object_fct.js](103-object_fct.js)
Update this script by adding a new function  `incr`  that increments the integer  `value`.

```
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$ 
```

> Written with [StackEdit](https://stackedit.io/).
