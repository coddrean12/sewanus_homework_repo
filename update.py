#!C:\Users\HODEWU\Documents\Web_backend\Python\mysql_env\Scripts\python.exe
print("Content-Type: text/html\n\n")

import mysql.connector, cgi
from mysql.connector import Error   

print("""
          <form action = "" method = "post">
        <label for="id">Record id to Update<label>
        <input type="text" id ="id" name="id"><br><br>
      
        <input type="submit" name="action" value="Update">

    </form>
             <form action="" method = "post">
        <label for="name">Enter an id to be updated:</label>
      <input type="text" id ="id" name="id"><br><br>

        <label for="recipe_name">Recipe name:</label>
        <input id="recipe_name" name="recipe_name" required><br><br>
      
        <label for="ingredients">Ingredients:</label>
        <textarea id="ingredients" name="ingredients" required><br><br>
      
        <label for="steps">Steps:</label>
        <textarea id="steps" name="steps" required><br><br>
    
        <input type="submit" name="action" value="Update">
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

    #Update operation
    elif action == "Update" and record_id:
        if recipe_name  or ingredients or steps:
            cursor.execute("""Update  SET recipe_name= %s,ingredients = %s,steps= %s Where id = %s""", (recipe_name, ingredients, steps, record_id))
            con.commit()
            print("<h1> RECORD UPDATED SUCCESFULLY </h1>")
        else:
            print("<h1> NO DATA PROVIDED FOR UPDATE </h1>")


except Error as e:
    print(f"<h1>Error: {e}</h1>")

except Exception as e:
    print(f"<h1>Error: {e}</h1>")

finally:
    if con.is_connected():
        cursor.close()
        con.close()