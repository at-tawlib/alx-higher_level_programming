# 0x0A-python-inheritance

## [0-lookup.py](0-lookup.py), [0-main.py](0-main.py)
returns the list of available attributes and methods of an object:
```
guillaume@ubuntu:~/0x0A$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
guillaume@ubuntu:~/0x0A$ 

```

## [1-my_list.py](1-my_list.py), [1-main.py](1-main.py)
has a class  `MyList`  that inherits from  `list`:
```
guillaume@ubuntu:~/0x0A$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
guillaume@ubuntu:~/0x0A$ 
```
## [2-is_same_class.py](2-is_same_class.py), [2-main.py](2-main.py)
has a function that returns  `True`  if the object is  _exactly_  an instance of the specified class ; otherwise  `False`.
```
guillaume@ubuntu:~/0x0A$ ./2-main.py
1 is an instance of the class int
guillaume@ubuntu:~/0x0A$ 
```
## [3-is_kind_of_class.py](3-is_kind_of_class.py), [3-main.py](3-main.py)
has a function that returns  `True`  if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise  `False`.
```
guillaume@ubuntu:~/0x0A$ ./3-main.py
1 comes from int
1 comes from object
guillaume@ubuntu:~/0x0A$ 
```

## [4-inherits_from.py](4-inherits_from.py), [4-main.py](4-main.py)
has a function that returns  `True`  if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise  `False`
```
guillaume@ubuntu:~/0x0A$ ./4-main.py
True inherited from class int
True inherited from class object
guillaume@ubuntu:~/0x0A$ 
```
## [5-base_geometry.py](5-base_geometry.py), [5-main.py](5-main.py)
has an empty class  `BaseGeometry`.
```
guillaume@ubuntu:~/0x0A$ ./5-main.py
<5-base_geometry.BaseGeometry object at 0x7f2050c69208>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
guillaume@ubuntu:~/0x0A$ 
```

## [6-base_geometry.py](6-base_geometry.py), [6-main.py](6-main.py)
has a class  `BaseGeometry`  (based on  [5-base_geometry.py](5-base_geometry.py)
```
guillaume@ubuntu:~/0x0A$ ./6-main.py
[Eception] area() is not implemented
guillaume@ubuntu:~/0x0A$ 
```

## [7-base_geometry.py](7-base_geometry.py), [7-main.py](7-main.py)
has a class  `BaseGeometry`  (based on  [6-base_geometry.py](6-base_geometry.py)).
```
guillaume@ubuntu:~/0x0A$ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
guillaume@ubuntu:~/0x0A$ 
```

## [8-rectangle.py](8-rectangle.py), [8-main.py](8-main.py)
has a class  `Rectangle`  that inherits from  `BaseGeometry`  ([7-base_geometry.py](7-base_geometry.py)).
```
guillaume@ubuntu:~/0x0A$ ./8-main.py
<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
guillaume@ubuntu:~/0x0A$ 
```
## [9-rectangle.py](9-rectangle.py), [9-main.py](9-main.py)
has a class  `Rectangle`  that inherits from  `BaseGeometry`  ([7-base_geometry.py](7-base_geometry.py)). (task based on [8-rectangle.py](8-rectangle.py))
```
guillaume@ubuntu:~/0x0A$ ./9-main.py
[Rectangle] 3/5
15
guillaume@ubuntu:~/0x0A$ 
```

## [10-square.py](10-square.py), [10-main.py](10-main.py)
has a class  `Square`  that inherits from  `Rectangle`  ([9-rectangle.py](9-rectangle.py)):
```
guillaume@ubuntu:~/0x0A$ ./10-main.py
[Rectangle] 13/13
169
guillaume@ubuntu:~/0x0A$ 
```
## [11-square.py](11-square.py), [11-main.py](11-main.py)
has a class  `Square`  that inherits from  `Rectangle`  ([9-rectangle.py](9-rectangle.py)). (task based on  [10-square.py](10-square.py)).
```
guillaume@ubuntu:~/0x0A$ ./11-main.py
[Square] 13/13
169
guillaume@ubuntu:~/0x0A$ 
```
## [100-my_int.py](100-my_int.py), [100-main.py](100-main.py)
has a class  `MyInt`  that inherits from  `int`:

-   `MyInt`  is a rebel.  `MyInt`  has  `==`  and  `!=`  operators inverted
```
guillaume@ubuntu:~/0x0A$ ./100-main.py
3
False
True
guillaume@ubuntu:~/0x0A$ 
```

## [101-add_attribute.py](101-add_attribute.py), [101-main.py](101-main.py)
has a function that adds a new attribute to an object if it’s possible:
```
guillaume@ubuntu:~/0x0A$ ./101-main.py
John
[TypeError] can't add new attribute
guillaume@ubuntu:~/0x0A$ 
```


> Written with [StackEdit](https://stackedit.io/).
