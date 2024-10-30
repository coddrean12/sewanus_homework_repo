#!C:\Users\HODEWU\Documents\Web_backend\Python\mysql_env\Scripts\python.exe
print("Content-Type: text/html\n\n")

import mysql.connector, cgi
from mysql.connector import Error   

print("""
          <form action = "" method = "post">
        <label for="id">Record id to Delete: <label>
        <input type="text" id ="id" name="id"><br><br>

        <input type="submit" name="action" value="Delete">
    </form>
      """)


form = cgi.FieldStorage()

recipe_name = form.getvalue("recipe_name")
ingredients = form.getvalue("ingredients")
steps = form.getvalue("steps")
record_id = form.getvalue("id")
action = form.getvalue("action")

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="",
        database="recipe_boook"
    )

    cursor = con.cursor()

    #DELETE operation
    elif action == "Delete" and record_id:
        cursor.execute("DELETE FROM book WHERE id = %s", (record_id,))
        con.commit()
        print("<h1>RECORED DELETED SUCCESFULLY</h1>")


except Error as e:
    print(f"<h1>Error: {e}</h1>")

except Exception as e:
    print(f"<h1>Error: {e}</h1>")

finally:
    if con.is_connected():
        cursor.close()
        con.close()