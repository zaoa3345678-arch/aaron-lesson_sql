import sqlite3

#connect to sql and get the permission
conn = sqlite3.connect('product_info.db')
cursor = conn.cursor()

# using permission to execute sql instruction
sqlsel="""
SELECT id, name FROM product_info
WHERE id='2'
"""
cursor.execute(sqlsel)

# grab execution result and save to python variable, print variable
records = cursor.fetchall()
print (records)


# execute sqlctrl.py
#1: in terminal: python sqlctrl.py
#2: in terminal: python3 sqlctrl.py
#3: in VSCode: click 'Run Python File'

