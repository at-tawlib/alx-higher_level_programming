# 0x0F. Python - Object-relational mapping

## [0-select_states.py](0-select_states.py) , [0-select_states.sql](0-select_states.sql)
script that lists all  `states`  from the database  `hbtn_0e_0_usa`:
-  script should take 3 arguments:  `mysql username`,  `mysql password`  and  `database name`  (no argument validation needed)
-   must use the module  `MySQLdb`  (`import MySQLdb`)
-   script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   Results must be sorted in ascending order by  `states.id`
-   Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
## [1-filter_states.py](1-filter_states.py), [0-select_states.sql](0-select_states.sql)
a script that lists all  `states`  with a  `name`  starting with  `N`  (upper N) from the database  `hbtn_0e_0_usa`:
-   script should take 3 arguments:  `mysql username`,  `mysql password`  and  `database name`  (no argument validation needed)
-   must use the module  `MySQLdb`  (`import MySQLdb`)
-   script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   Results must be sorted in ascending order by  `states.id`
-   Results must be displayed as they are in the example below
-   code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
## [2-my_filter_states.py](2-my_filter_states.py), [0-select_states.sql](0-select_states.sql)
script that takes in an argument and displays all values in the  `states`  table of  `hbtn_0e_0_usa`  where  `name`  matches the argument.
-   script should take 4 arguments:  `mysql username`,  `mysql password`,  `database name`  and  `state name searched`  (no argument validation needed)
-   Your script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   You must use  `format`  to create the SQL query with the user input
-   Results must be sorted in ascending order by  `states.id`
-   Results must be displayed as they are in the example below
-   Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
## [3-my_safe_filter_states.py](3-my_safe_filter_states.py), [0-select_states.sql](0-select_states.sql)
In the above we did not check for SQL injection hence all the records will be deleted if the following code is run
```
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
```
Yes, it’s an [SQL injection](https://intranet.alxswe.com/rltoken/qzLjdkHPTue2U1isMj5fJA "SQL injection") to delete all records of a table…
Once again, write a script that takes in arguments and displays all values in the  `states`  table of  `hbtn_0e_0_usa`  where  `name`  matches the argument. But this time, write one that is safe from MySQL injections!
-   script should take 4 arguments:  `mysql username`,  `mysql password`,  `database name`  and  `state name searched`  (safe from MySQL injection)
-   You must use the module  `MySQLdb`  (`import MySQLdb`)
-   Your script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   Results must be sorted in ascending order by  `states.id`
-   Results must be displayed as they are in the example below
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
## [4-cities_by_state.py](4-cities_by_state.py) , [4-cities_by_state.sql](4-cities_by_state.sql)
script that lists all  `cities`  from the database  `hbtn_0e_4_usa`
-   script should take 3 arguments:  `mysql username`,  `mysql password`  and  `database name`
-   script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   Results must be sorted in ascending order by  `cities.id`
```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
## [5-filter_cities.py](5-filter_cities.py) , [4-cities_by_state.sql](4-cities_by_state.sql)
script that takes in the name of a state as an argument and lists all  `cities`  of that state, using the database  `hbtn_0e_4_usa`
-   script takes 4 arguments:  `mysql username`,  `mysql password`,  `database name`  and  `state name`  (SQL injection free!)
-   script  connects to a MySQL server running on  `localhost`  at port  `3306`
-   Results sorted in ascending order by  `cities.id`
```
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/0x0F$  
```
