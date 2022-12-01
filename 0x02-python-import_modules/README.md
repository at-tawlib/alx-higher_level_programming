# 0x02. Python - import & modules


## `0-add.py`, `add_0.py`
a program that imports the function  `def add(a, b):`  from the file  `add_0.py`  and prints the result of the addition  `1 + 2 = 3`
```
guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py 
guillaume@ubuntu:~/0x02$ 
```

##  `1-calculation.py`,  `calculator_1.py`
a program that imports functions from the file  `calculator_1.py` , does some Maths, and prints the result.

```
guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$
```

  




a program that prints the number of and the list of its arguments.
```
guillaume@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/0x02$ 
```
## `2-args.py`
Write a program that prints the result of the addition of all arguments

-   The output should be the result of the addition of all arguments, followed by a new line
-   You can cast arguments into integers by using  `int()`  (you can assume that all arguments can be casted into integers)
-   Your code should not be executed when imported

```
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
guillaume@ubuntu:~/0x02$ 
```




> Written with [StackEdit](https://stackedit.io/).
