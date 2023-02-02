# Description
This is a small project that allows me to load excel sheets into a postgres database. Since this was made as a result of a task for my interview. This version is limited in ability, but can be updated easily.

Some things are currently hardcoded:
-It will read only the first sheet of the excel file
-It uses a prewritten header for the sheet and columns when creating new table


# Requirements
Have Python3 installed
Have Postgresql installed (I used version 15.1.)

Install 3 packages: **pandas, psycopg2, openpyxl**
-recommended to use 'pip install'

# Get started
 Open [database.ini](https://github.com/Antisa184/Python_task/blob/main/database.ini) and edit the password to whatever you set for your default
postgres database.

Put xlsx file inside the root folder of the project
Start [main.py](https://github.com/Antisa184/Python_task/blob/main/main.py) with 'py main.py' and follow the instructions!

**Enjoy!**

