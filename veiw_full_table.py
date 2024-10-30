#!C:\Users\HODEWU\Documents\Web_backend\Python\mysql_env\Scripts\python.exe
print("Content-Type: text/html\n\n")

import mysql.connector, cgi
from mysql.connector import Error

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

    cursor = con.cursor(dictionary=True)

    if action == "View" and record_id:
        cursor.execute("SELECT * FROM book")
        results = cursor.fetchall()
        if results:
             
            print("""<table width='57%' border='1'>
                    <caption>Read Recipes</caption>
                    <tr>
                        <th>Recipe name</th>
                        <th>Indgredients</th>
                        <th>Steps</th>
                    </tr>""")

            for result in results:
                
                print(f""" 
                    <tr>
                        <td>{result['recipe_name']}</td>
                        <td>{result['ingredients']}</td>
                        <td>{result['steps']}</td>
                    </tr>
                </table>
                    """)

except Error as e:
    print(f"<h1>Error: {e}</h1>")

except Exception as e:
    print(f"<h1>Error: {e}</h1>")

finally:
    if con.is_connected():
        cursor.close()
        con.close()