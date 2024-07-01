#!C:\Users\abhis\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import mysql.connector 
from mysql.connector import Error
import cgitb

# Enable detailed error reporting
cgitb.enable()

# Send HTTP header
print("Content-type: text/html\n\n")

# Connect to the database
# Get form data
form = cgi.FieldStorage()
name = form.getvalue('Name')
email = form.getvalue('Email')
college = form.getvalue('College')
event = form.getvalue('Event')

# Connect to the database
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='euphoria_db',
        user='root',
        password=''
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)

# Insert a new student
try:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO registration (name, email, college, event) VALUES (%s, %s, %s, %s)", (name, email, college, event))
    connection.commit()
except Error as e:
    print("Error while inserting data to MySQL", e)

# Close the connection
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



# Display a message
print("<h1>Student added successfully!</h1>")
print("<p>Name: %s</p>" % name)
print("<p>Email: %s</p>" % email)
print("<p>College: %s</p>" % college)
print("<p>Event: %s</p>" % event)



