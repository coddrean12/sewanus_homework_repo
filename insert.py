#!C:\Users\HODEWU\Documents\Web_backend\Python\mysql_env\Scripts\python.exe
print("Content-Type: text/html\n\n")

import mysql.connector, cgi
from mysql.connector import Error   

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css"/>
    <title>Document</title>
</head>
<body>
    <h1 class="h1">Recipe Book</h1>
    <div>
<form action = "veiw.py" method = "post">
    <input for="id" class="searchrecipe" placeholder="Search recipe..." />
    <button class="searchrecipebutton type="submit" name="action" >SEARCH</button>
    </form>
</div>


<div class="box">


    <h1 class="h12">Add Recipe</h1>
      <form name="contact" method= "POST" action= "">
    <li><input class="addrecipe" name="recipe_name" type="text" placeholder="Recipe name"/></li>
    <li><textarea class="addrecipe" name="ingredients" type="text" placeholder="Ingeridents ( comma seperated )"/></textarea></li>
    <li><textarea class="addrecipe" name="steps" type="text" placeholder="Steps"/></textarea></li>
    <button class="addrecipebutton" type="submit">Add Recipe</button>
    <a class="addrecipebutton" href="update.py">UPDATE </a>
    <a class="addrecipebutton" href="veiw_full_table.py">VIEW </a>
      </form>
</div>

</body>
</html>
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

    if recipe_name and ingredients and steps and not record_id:
        cursor.execute("INSERT INTO book (recipe_name, ingredients, steps) VALUES (%s, %s, %s)", (recipe_name, ingredients, steps))
        con.commit()
        print("<h1> RECORD INSERTED SUCCESFULLY </h1>")

except Error as e:
    print(f"<h1>Error: {e}</h1>")

except Exception as e:
    print(f"<h1>Error: {e}</h1>")

finally:
    if con.is_connected():
        cursor.close()
        con.close()