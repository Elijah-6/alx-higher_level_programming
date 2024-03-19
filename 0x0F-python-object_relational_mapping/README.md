## 0x0F-python-object_relational_mapping
Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
Also, you can have this warning message:

/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)


Certainly! Below is the documentation for the Python scripts I provided earlier:

---

## Script 1: Retrieve All States from Database

### Description:
This script connects to a MySQL server and retrieves all states from the `hbtn_0e_0_usa` database. The results are sorted in ascending order by `states.id` and displayed as specified.

### Usage:
1. Make sure you have the `MySQLdb` module installed (`pip install MySQL-python`).
2. Replace the placeholders for `username`, `password`, and `db_name` with your actual MySQL credentials.
3. Run the script with the following command:
   ```
   python script1.py <username> <password> <db_name>
   ```

### Example Output:
```
(1, 'Alabama')
(2, 'Alaska')
(3, 'Arizona')
...
```

---

## Script 2: Retrieve States Starting with 'N'

### Description:
This script connects to a MySQL server and retrieves all states from the `hbtn_0e_0_usa` database whose names start with an uppercase 'N'. The results are sorted in ascending order by `states.id` and displayed as specified.

### Usage:
1. Make sure you have the `MySQLdb` module installed (`pip install MySQL-python`).
2. Replace the placeholders for `username`, `password`, and `db_name` with your actual MySQL credentials.
3. Run the script with the following command:
   ```
   python script2.py <username> <password> <db_name>
   ```

### Example Output:
```
(27, 'Nebraska')
(28, 'Nevada')
(29, 'New Hampshire')
...
```

---

## Script 3: Retrieve States by Name (Safe from Injections)

### Description:
This script connects to a MySQL server and retrieves all states from the `hbtn_0e_0_usa` database where the name matches the provided argument. It uses parameterized queries to prevent SQL injection. The results are sorted in ascending order by `states.id` and displayed as specified.

### Usage:
1. Make sure you have the `MySQLdb` module installed (`pip install MySQL-python`).
2. Replace the placeholders for `username`, `password`, `db_name`, and `search_name` with your actual MySQL credentials and the desired state name.
3. Run the script with the following command:
   ```
   python script3.py <username> <password> <db_name> <state_name>
   ```

### Example Output:
```
(5, 'California')
```

---

## Script 4: Retrieve All Cities from Database

### Description:
This script connects to a MySQL server and retrieves all cities from the `hbtn_0e_4_usa` database. The results are sorted in ascending order by `cities.id` and displayed as specified.

### Usage:
1. Make sure you have the `MySQLdb` module installed (`pip install MySQL-python`).
2. Replace the placeholders for `username`, `password`, and `db_name` with your actual MySQL credentials.
3. Run the script with the following command:
   ```
   python script4.py <username> <password> <db_name>
   ```

### Example Output:
```
(1, 'New York')
(2, 'Los Angeles')
(3, 'Chicago')
...
```

---

Remember not to execute the code when importing it. If you have any further questions or need assistance, feel free to ask! 🍀
