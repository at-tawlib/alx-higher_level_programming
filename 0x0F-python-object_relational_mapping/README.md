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

## [model_state.py](model_state.py), [6-model_state.sql](6-model_state.sql), [6-model_state.py](6-model_state.py)
`model_state.py` contains the class definition of a  `State`  and an instance  `Base = declarative_base()`:
-   Your script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   **WARNING:**  all classes who inherit from  `Base`  **must**  be imported before calling  `Base.metadata.create_all(engine)`
```
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/0x0F$ 
```

## [7-model_state_fetch_all.py](7-model_state_fetch_all.py) , [7-model_state_fetch_all.sql](7-model_state_fetch_all.sql)
script that lists all  `State`  objects from the database  `hbtn_0e_6_usa`
-   script takes 3 arguments:  `mysql username`,  `mysql password`  and  `database name` using the module  `SQLAlchemy`
-   script connects to a MySQL server running on  `localhost`  at port  `3306`
-   Results sorted in ascending order by  `states.id`
```
guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```
## [8-model_state_fetch_first.py](8-model_state_fetch_first.py)
script that prints the first  `State`  object from the database  `hbtn_0e_6_usa`
-   script takes 3 arguments:  `mysql username`,  `mysql password`  and  `database name`
-   script connects to a MySQL server running on  `localhost`  at port  `3306`
-   The state you display must be the first in  `states.id`
-   If the table  `states`  is empty, print  `Nothing`  followed by a new line
```
guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$ 
```
## [9-model_state_filter_a.py](9-model_state_filter_a.py)
script that lists all  `State`  objects that contain the letter  `a`  from the database  `hbtn_0e_6_usa`
-   script takes 3 arguments:  `mysql username`,  `mysql password`  and  `database name`
-   Your script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   Results sorted in ascending order by  `states.id`
```
guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```
## [10-model_state_my_get.py](10-model_state_my_get.py)
script that prints the  `State`  object with the  `name`  passed as argument from the database  `hbtn_0e_6_usa`
-  script  takes 4 arguments:  `mysql username`,  `mysql password`,  `database name`  and  `state name to search`  (SQL injection free)
-   script connects to a MySQL server running on  `localhost`  at port  `3306`
-   assume you have one record with the state name to search
-   Results must display the  `states.id`
-   If no state has the name you searched for, display  `Not found`
```
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/0x0F$ 
```
## [11-model_state_insert.py](11-model_state_insert.py)
script that adds the  `State`  object “Louisiana” to the database  `hbtn_0e_6_usa`
-   script takes 3 arguments:  `mysql username`,  `mysql password`  and  `database name`
-   script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   Print the new  `states.id`  after creation
```
guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
```
## [12-model_state_update_id_2.py(12-model_state_update_id_2.py)
script that changes the name of a  `State`  object from the database  `hbtn_0e_6_usa`
-   script  takes 3 arguments:  `mysql username`,  `mysql password`  and  `database name`
-   script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   Change the name of the  `State`  where  `id = 2`  to  `New Mexico`
```
guillaume@ubuntu:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
```
## [13-model_state_delete_a.py](13-model_state_delete_a.py)
script that deletes all  `State`  objects with a name containing the letter  `a`  from the database  `hbtn_0e_6_usa`
-   script  takes 3 arguments:  `mysql username`,  `mysql password`  and  `database name`
-   script connects to a MySQL server running on  `localhost`  at port  `3306`
```
guillaume@ubuntu:~/0x0F$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
guillaume@ubuntu:~/0x0F$ 
```
## [model_city.py](model_city.py) 
file similar to  [model_state.py](model_state.py)  named  `model_city.py`  that contains the class definition of a  `City`.
-   `City`  class:
    -   inherits from  `Base`  (imported from  `model_state`)
    -   links to the MySQL table  `cities`
   
##  [14-model_city_fetch_by_state.py](14-model_city_fetch_by_state.py), [14-model_city_fetch_by_state.sql](14-model_city_fetch_by_state.sql)
prints all  `City`  objects from the database  `hbtn_0e_14_usa`:
-   script takes 3 arguments:  `mysql username`,  `mysql password`  and  `database name`
-  script should connect to a MySQL server running on  `localhost`  at port  `3306`
-   Results sorted in ascending order by  `cities.id`
```
guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
guillaume@ubuntu:~/0x0F$ 
```
> Written with [StackEdit](https://stackedit.io/).
