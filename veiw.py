#!C:\Users\HODEWU\Documents\Web_backend\Python\mysql_env\Scripts\python.exe
print("Content-Type: text/html\n\n")

import mysql.connector, cgi
from mysql.connector import Error   

print("""
          <form action = "" method = "post">
        <label for="id">Record id to Update/Delete: <label>
        <input type="text" id ="id" name="id"><br><br>
        <input type="submit" name="action" value="View">
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

#Read operation
    if action == "View" and record_id:
        cursor.execute("SELECT * FROM book WHERE id = %s", (record_id,))
        result = cursor.fetchone()
        if result: 
            print(f"<h1>Record id {record_id}</h1>")
            print(f"""
                  recipe name | ingredients | steps
                {result[1]} | {result[2]} | {result[3]} """)

            print(f""" 
                <table width='70%' border='1'>
                <caption>Read Recipes </caption>
                <tr>
                    <th>Recipe name</th>
                    <th>Indgredients</th>
                    <th>Steps</th>
                </tr>
                <tr>
                    <td>{result[1]}</td>
                    <td>{result[2]}</td>
                    <td>{result[3]}</td>
                </tr>
            </table>
                            """)
        else:
                print("<h1>Record not found</h1>")


except Error as e:
    print(f"<h1>Error: {e}</h1>")

except Exception as e:
    print(f"<h1>Error: {e}</h1>")

finally:
    if con.is_connected():
        cursor.close()
        con.close()