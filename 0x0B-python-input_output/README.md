# 0x0B. Python - Input/Output
## [0-read_file.py](0-read_file.py), [0-main.py](0-main.py)
has a function that reads a text file (`UTF8`) and prints it to stdout:
```
guillaume@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ 
```

## [1-write_file.py](1-write_file.py), [1-main.py](1-main.py)
has a function that writes a string to a text file (`UTF8`) and returns the number of characters written:
```
guillaume@ubuntu:~/0x0B$ ./1-main.py
29
guillaume@ubuntu:~/0x0B$ cat my_first_file.txt
This School is so cool!
guillaume@ubuntu:~/0x0B$ 
```
## [2-append_write.py](2-append_write.py), [2-main.py](2-main.py)
has a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:
```
cat: file_append.txt: No such file or directory
guillaume@ubuntu:~/0x0B$ ./2-main.py
29
guillaume@ubuntu:~/0x0B$ cat file_append.txt
This School is so cool!
guillaume@ubuntu:~/0x0B$ ./2-main.py
29
guillaume@ubuntu:~/0x0B$ cat file_append.txt
This School is so cool!
This School is so cool!
guillaume@ubuntu:~/0x0B$ 
```

## [3-to_json_string.py](3-to_json_string.py), [3-main.py](3-main.py)
has a function that returns the JSON representation of an object (string):
```
guillaume@ubuntu:~/0x0B$ ./3-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
<class 'str'>
[TypeError] {3, 132} is not JSON serializable
guillaume@ubuntu:~/0x0B$ 
```

## [4-from_json_string.py](4-from_json_string.py), [4-main.py](4-main.py)
has a function that returns an object (Python data structure) represented by a JSON string:
```
guillaume@ubuntu:~/0x0B$ ./4-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
guillaume@ubuntu:~/0x0B$ 
```

## [5-save_to_json_file.py](5-save_to_json_file.py), [5-main.py](5-main.py)
has a function that writes an Object to a text file, using a JSON representation:
```
guillaume@ubuntu:~/0x0B$ ./5-main.py
[TypeError] {3, 132} is not JSON serializable
guillaume@ubuntu:~/0x0B$ cat my_list.json ; echo ""
[1, 2, 3]
guillaume@ubuntu:~/0x0B$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
guillaume@ubuntu:~/0x0B$ cat my_set.json ; echo ""

guillaume@ubuntu:~/0x0B$ 
```
## [6-load_from_json_file.py](6-load_from_json_file.py), [6-main.py](6-main.py)
has a function that creates an Object from a “JSON file”:
```
guillaume@ubuntu:~/0x0B$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
guillaume@ubuntu:~/0x0B$ 
```
## [7-add_item.py](7-add_item.py), [7-main.py](7-main.py)
has a script that adds all arguments to a Python list, and then save them to a file:
```
guillaume@ubuntu:~/0x0B$ cat add_item.json
cat: add_item.json: No such file or directory
guillaume@ubuntu:~/0x0B$ ./7-add_item.py
guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
[]
guillaume@ubuntu:~/0x0B$ ./7-add_item.py Best School
guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
["Best", "School"]
guillaume@ubuntu:~/0x0B$ ./7-add_item.py 89 Python C
guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]
guillaume@ubuntu:~/0x0B$ 
```


## [8-class_to_json.py](8-class_to_json.py), [8-main.py](8-main.py)
has a function that returns the dictionary description with simple data sructure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
```
guillaume@ubuntu:~/0x0B$ ./8-main.py 
<class '8-my_class.MyClass'>
[MyClass] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}
guillaume@ubuntu:~/0x0B$ 
guillaume@ubuntu:~/0x0B$ ./8-main_2.py 
<class '8-my_class_2.MyClass'>
[MyClass] John - 4 => 1
<class 'dict'>
{'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
guillaume@ubuntu:~/0x0B$
```
## [9-student.py](9-student.py), [9-main.py](9-main.py)
has a class  `Student`  that defines a student
```
guillaume@ubuntu:~/0x0B$ ./9-main.py 
<class 'dict'>
John
<class 'str'>
23
<class 'int'>
<class 'dict'>
Bob
<class 'str'>
27
<class 'int'>
guillaume@ubuntu:~/0x0B$ 
```

## [10-student.py](10-student.py), [10-main.py](10-main.py)
has a class  `Student`  that defines a student (based on  [9-student.py](9-student.py))
-   `def to_json(self, attrs=None):`  that retrieves a dictionary representation of a  `Student`  instance (same as  [8-class_to_json.py](8-class_to_json.py)):
    -   If  `attrs`  is a list of strings, only attribute names contained in this list must be retrieved.
    -   Otherwise, all attributes must be retrieved
```
guillaume@ubuntu:~/0x0B$ ./10-main.py 
{'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
{'age': 27, 'first_name': 'Bob'}
{'age': 27}
guillaume@ubuntu:~/0x0B$
```
## [11-student.py](11-student.py), [11-main.py](11-main.py)
has a class  `Student`  that defines a student by: (based on  [10-student.py](10-student.py))
-   Public method  `def reload_from_json(self, json):`  that replaces all attributes of the  `Student`  instance:
    -   You can assume  `json`  will always be a dictionary
    -   A dictionary key will be the public attribute name
    -   A dictionary value will be the value of the public attribute
```
guillaume@ubuntu:~/0x0B$ ./11-main.py student.json
Initial student:
<11-student.Student object at 0x7f832826eda0>
<class '11-student.Student'>
<class 'dict'>
John Doe 23
{"last_name": "Doe", "first_name": "John", "age": 23}
Saved to disk
Fake student:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
Fake Fake 89
Load dictionary from file:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
John Doe 23
guillaume@ubuntu:~/0x0B$ cat student.json ; echo ""
{"last_name": "Doe", "first_name": "John", "age": 23}
guillaume@ubuntu:~/0x0B$ 
```

## [12-pascal_triangle.py](12-pascal_triangle.py), [12-main.py](12-main.py)
**Technical interview preparation**:
Create a function  `def pascal_triangle(n):`  that returns a list of lists of integers representing the Pascal’s triangle of  `n`:

-   Returns an empty list if  `n <= 0`
-   You can assume  `n`  will be always an integer
```
guillaume@ubuntu:~/0x0B$ 
guillaume@ubuntu:~/0x0B$ ./12-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x0B$ 
```
> Written with [StackEdit](https://stackedit.io/).t
