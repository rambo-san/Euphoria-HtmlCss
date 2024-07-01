#!C:\Users\abhis\AppData\Local\Programs\Python\Python312\python.exe
import mysql.connector
from mysql.connector import Error
import cgitb
import cgi

print("Content-type: text/html\n\n")
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='euphoria_db',
        user='root',
        password=''
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM registration")
        rows = cursor.fetchall()
        print("<table border='1'>")
        print("<tr>")
        print("<th>Name</th>")
        print("<th>Email</th>")
        print("<th>College</th>")
        print("<th>Event</th>")
        print("<th>Time</th>")
        print("</tr>")
        for row in rows:
            print("<tr><td>%s</td>" % row[0])
            print("<td>%s</td>" % row[1])
            print("<td>%s</td>" % row[2])
            print("<td>%s</td>" % row[3])
            print("<td>%s</td></tr>" % row[4])
            print("<td><button onclick='delete_row(%s)'>Delete</button></td></tr>" % row[0])
        print("</table>")

        cursor.close()
        connection.close()
    else:
        print("Connection to MySQL is not established.")
except Error as e:
    print("Error while connecting to MySQL", e)

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM your_table_name")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        connection.close()
    else:
        print("Connection to MySQL is not established.")

def delete_row(id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='euphoria_db',
            user='root',
            password=''
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("DELETE FROM registration WHERE id = %s", (id))
            connection.commit()
            print("<alert>Row deleted successfully</alert>")
        else:
            print("Connection to MySQL is not established.")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        else:
            print("Connection to MySQL is not established.")