## MySQL

In our current version of the website, we're getting the items of the To-Do list from a python script `data.py`, which is not practical. Normally, we'd like to store the user data in a database, that is more secure, less prone to errors and can store a larger amount of data. So as an example, we'll store the To-Do list in aMySQLdatabase. For more information aboutMySQLdatabase, visit the official [website](https://www.tutorialspoint.com/mysql/mysql-introduction.htm).

### Installation

#### Linux

In Linux, the installation is quite straight forward, all we need To-Do is call apache package manager, and install both the client and server versions of MySQL:

```
sudo apt-get install mysql-server libmysqlclient-dev
```

We'll use to access our MySQL server, to create a database, and in this database we can then create different Tables (e.g. users, articles, projects, todo list ...), and also use it from our python script to add / remove / edit some element of a given Table we've created.

To login to our database, we provide the user `-u root`, make sure you run it as a root user since it is new installation:

```
sudo mysql -u root 
```

### Setting a password for the root user
It is always a good idea to secure the database, so let's add a password for the `root` user, within the MySQL terminal, let's execute the following commands, replace `NewPassword` in the second command with your password of choice.

```shell
mysql> USE mysql;
mysql> UPDATE user SET authentication_string=PASSWORD("NewPassword") WHERE User='root';
mysql> FLUSH PRIVILEGES;
mysql> exit;
```

And then restart the server: `$ service mysql restart`, and now make sure you can access MySQL using the new password, run `mysql -u root -p`.

#### Windows

Download the MySQL installation from the official [website](https://dev.mysql.com/downloads/file/?id=490395). Then simply install it using the default options.
Note that you'll be asked for the root password at some point, make sure to remeber it.

After the installtion is finished (can take some time, ~ 20 min). We need to launch the installed MySQL shell, in the search bar, search for MySQL and launch `MySQL 8.0 Command Line Client`.
You'll be asked for a the root password, use the password
you've added during the installation to connect. Now all of  the following MySQL commands will work within this client shell.


### Database creation

Now that we logged into the database, we can see the databases:

```shell
SHOW DATABASES;
```

Let's create a new database called `codingweeks` and access it

```shell
CREATE DATABASE codingweeks;

USE codingweeks;
```

Now let's create a new table `todolist`, with the following fields :
- `id`: and int up to 11 numbers, automatically incremented when a new element in added, and it will be our primary key.
- `title`: the title of the To-Do task, a char with a maximum of 255 characters.
- `author`: the author of the To-Do list, a char with a maximum of 100 characters.
- `task`: a description of the task to be done, an unlimited Text field.
- `create_date`: a time stamp, will be created automatically with the current date.

You can add any additional field you think is missing (like `assigned to`, `done`). 

This can be added using the following MySQL command:

```shell
CREATE TABLE todolist (id INT(11) AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(100), task TEXT, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

Now we can see the table we've created:

```
SHOW TABLES;
```

And if you want to delete the table and start again, you can drop it using the following command:

```shell
DROP TABLE todolist;
```

### Using the database

Now the main objective is to display the items of the To-Do list from the `todolist` table in the database from website's `todo` page, and also have the possibility of adding and editing / deleting the existing items of the database table from within our website.

So after we've installed MySQL, and after creating our database and the table we'll use, we then need to install flask database package to communicate with MySQL from our flask app. In your virtualenv, install `flask-mysqldb`. We'll also need Flask forms to add and edit items of our To-Do list:

```
pip install flask-mysqldb
pip install Flask-WTF
```

Now we'll import the installed packages and use them in our flask app:

```python
from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
```

Now let's create a connection to our local MySQL database, for this we'll need the host-name (or IP address). Given that we've created the database locally, we'll use `localhost` (i.e. 127.0.0.1), we'll also need the user-name and password to the MySQL session (`root` and the password we've used when installing mysql), the name of the database we'd like to access (in our case `codingweeks`), and the type of the cursor we'd like to use to access the database (`DictCursor`).

```python
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'codingweeks'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)
```

In the html file of the `todo` page, let's add an `ADD` button using a bootstrap class, here we use `btn-success`, you can use another type of button if you like ([Bootstrap Buttons](https://getbootstrap.com/docs/4.0/components/buttons/)), the positioning and style of the Button is up to you:

```html
<a class="btn btn-success" href="/add_item"> Add Item</a>
```

This button we'll direct us into `/add_item`

To add an item to the to-do list, we'll need a form, to create a form we'll use `Flask-WTF`, which is a thin wrapper around the WTForms package that nicely integrates it with Flask. This is another flask extension (together with `flask-mysqldb`). Extensions are a very important part of the Flask ecosystem, as they provide solutions to problems that Flask is intentionally not opinionated about. We create a simple item class, with three fields, one for the title of type string, with a maximum length of 200 characters, the same for the author field with a max of 100. And a task field with text type, with a minimum of 30.

```python
# Item Form Class
class ItemForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    author = StringField('Author', [validators.Length(min=1, max=100)])
    task = TextAreaField('Task', [validators.Length(min=30)])
```

We also need to create a route to the item creation page `/add_item`. This time we'll use a new functionality, which is `HTTP Methods`. In addition to accepting the URL of a route as a parameter, Route decorators (`@app.route`) can accept a second parameter: a list of accepted HTTP Methods. By default, a Flask route accepts all methods on a route (GET, POST, etc). Providing a list of accepted methods is a good way to build constraints into the route for a REST API end-point (in the next tutorial we'll get into more details about this) which only makes sense in specific contexts. We'll use to HTTP methods:

- GET: used to request data from a specified resource. Used to simply render the page, this is the default behavior for all the pages we've created thus far.
- POST: used to send data to a server to create / update a resource. We'll use it to add an new item from the server to the database.

```python
# Add Item tp the To-Do list
@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = ItemForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        author = form.author.data
        task = form.task.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO todolist(title, task, author) VALUES(%s, %s, %s)",(title, task, author))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()
        flash('Item Added to the to-do list', 'success')
        return redirect(url_for('home'))

    return render_template('add_item.html', form=form)
```

In the code above, if the method is POST, in this case, we're adding a new item to our `todo` list. Ssing the initilized MySQL database instance, we'll create a new cursor, execute a MySQL command to insert the passed item into the `todolist` table we've create. Then commit it and close the connection, flash a success message (here we'll use our `includes/_messages.html` file) and return to the home page. If we get a GET method, we simply render the `add_item` page.

Now we'll need to create the `add_item.html` file, in `templates`, create the html file and add a simple HTML web-from using some bootstrap classes, you'll need to complete the rest of the form fields, just like we did for the first item `title`:

```html
{% extends 'layout.html' %}

{% block body %}
  <h1>Add TO-DO list item</h1>
  {% from "includes/_formhelpers.html" import render_field %}
  <form method="POST" action="">
    <div class="form-group">
      {{ render_field(form.title, class_="form-control") }}
    </div>

    <-- ADD THE REST OF THE FORM ITEMS -->

    <p><input class="btn btn-primary" type="submit" value="Submit">
  </form>
{% endblock %}
```

In the script above, you'll see that we've included a new file called `_formhelpers.html`, it is used to manage the forms errors (if we provided some incorrect input in our forms). In `includes`, create a new file `_formhelpers.html`, and add the following (this snippet was taken from the official docs of [flask-wtforms](https://flask-wtf.readthedocs.io/en/stable/)).

```html
{% macro render_field(field) %}
  {{ field.label }}
  {{ field(**kwargs)|safe }}
  {% if field.errors %}
    {% for error in field.errors %}
      <span class="help-inline">{{ error }}</span>
    {% endfor %}
  {% endif %}
{% endmacro %}
```

If you try to add an item, you get a session error, this is because when we send the form to the Flask app, there is no encryption. But to have a safe-keeping mechanism against tampering by attackers, `Flask` requires us to set a secret key to our session, to do this add this two lines in before running the app:

```python
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
```

Now re-run the app, go to the web-page, add a new item, you must be redirected to the home page with a success notification message. Then go to the MySQL command line, use the database and type `SELECT * FROM todolist;`. Make sure the added item(s) is(are) in there.

### Adding a text editor

When adding the task description, we'd like to use a text editor. For this we'll use a 3rd party text editor called [ckeditor](https://ckeditor.com/). Just like we've done for bootstrap, we'll add the [CKEditor CDN](https://cdn.ckeditor.com/) to our `layout.html`. Let's add the following lines in `layout.html`:

```html
  <script src="//cdn.ckeditor.com/4.6.2/basic/ckeditor.js"></script>
  <script type="text/javascript">
    CKEDITOR.replace('editor')
  </script>
```

After adding CKEditor to our website, we can then apply it to all the tags with an attribute `id=editor` (due to this line `CKEDITOR.replace('editor')`). Now go to `add_item.html` and add a `id=editor` attribute to the `render_field`. Now go to add item page and you'll find that now we have a integrated a text editor in the task field.

### Listing the to-do items

Until now, the listed items in `todo` page are coming from `data.py`. We'd like to list the items in our database instead. We'll edit our function that renders the `todo` page in the main flask app `app.py`. Similar to `add_item`, we need to create a connection to our database, but this time instead of adding an new item to our table `todolist`, we fetch all the existing items, and then pass them to the rendering function. If no items were found, we'll display the corresponding message.

```python
# Dashboard
@app.route('/todo')
def todo():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get items
    result = cur.execute("SELECT * FROM todolist")
    items = cur.fetchall()

    # Close connection
    cur.close()

    if result > 0:
        return render_template('todo.html', items=items)
    else:
        msg = 'No Items Found'
        return render_template('todo.html', msg=msg)
```

Now let's go back to `todo.html`, and let's list the To-Do list items in a table. We'll have the Add-Item button we've added earlier. We create the table with a bootstrap class `table-striped`. The table we'll have a number of headings `<th> </th>` and then we loop through the passed items, each time adding a new element to the table using the cell tag `<td>`. See [mozilla devs](https://developer.mozilla.org/fr/docs/Web/HTML/Element/td) for an example.

```html
{% extends 'layout.html' %}

{% block body %}
  <h1>To-Do List</h1>
  <a class="btn btn-success" href="/add_item"> Add Item</a>
  <hr>
  <table class="table table-striped">
    <tr>
      <th>ID</th>
      <th>Title</th>
      <th>Author</th>
      <th>Date</th>
    </tr>
    {% for item in items %}
      <tr>
        <td>{{item.id}}</td>
        <td>{{item.title}}</td>
        <td>{{item.author}}</td>
        <td>{{item.create_date}}</td>
      </tr>
    {% endfor %}
  </table>
{% endblock %}
```

Now add a new item, and see if it shows up in the table.

### Single item page

Currently, if we access the web-page for a given item on the to-do list with a given ID (like `localhost:5000/items/100/`). Only the id is displayed. We'd like to show the task description instead and the rest of the item information. So let's edit the function `items(id)`. This time, we'll create a new database connection, and only fetch one to-do list item with the corresponding ID. Then render the page after we pass the item, if the item with the requested ID does not exists in our database, we'll return a message.

```python
#Single Item
@app.route('/todo/<string:id>/')
def items(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get item
    result = cur.execute("SELECT * FROM todolist WHERE id = %s", [id])

    item = cur.fetchone()

    return render_template('items.html', item=item)
```

Now go the `items.html`, instead of displaying only the ID. Display the passed fields (tile, task, author, create date) using some simple HTML tags. Add some bootstrap classes if you wish. Note that we add a pipe (`| safe`) to avoid seeing HTML tags on the displayed text.

```html
{% extends 'layout.html' %}

{% block body %}
  <h1>{{item.title}}</h1>
  <small>Written by {{item.author}} on {{item.create_date}}</small>
  <hr>
  <div>
    {{item.task | safe}}
  </div>
{% endblock %}
```

**Your turn:**

- Add an `href` to the title, so that when we click it we do to the item page (`todo/id`) 

- Now what if the item does not exist, in the function `items(id)`, instead of passing the item to the render function, pass an error message. And in the HTML file `items.html`. Using Jinja [Test statements](https://jinja.palletsprojects.com/en/2.10.x/templates/), display the passed error message if the passed item does not exit (for example a [404 page](https://bootsnipp.com/snippets/Qb71)).

Now test if the website is functioning correctly, add an item, see if we can see it in the To-Do list table. Then access a non existing item and see if the error message is displayed correctly.

### Editing and deleting items

Now from our `todo` page, we'd like to be able to edit the existing tasks, and also remove a given task from the to-do list. First step is to add `delete` and `edit` buttons in table of To-Do list items. In `todo.html` add the two following snippets in the correct positions:

- Two empty headings, for two buttons, edit and delete.
```html
  <th></th>
  <th></th>
```

- A bootstrap button with colors `default` (white) for editing, the Edit button will be right aligned using the option `pull-right`. See the bootstrap [docs](https://getbootstrap.com/docs/4.0/components/buttons/) for more examples. Wen we click the button, we'll be redirected into the Edit page with the corresponding item ID `edit_item/{{item.id}}`.
```html
  <td><a href="edit_item/{{item.id}}" class="btn btn-default pull-right">Edit</a></td>
```

- A second button, this time with color `danger` (red) for deleting the To-Do list item / task, the button is restricted to a POST request, so we'll wrap our button in a `form` tag. Given that we're not going to render any HTML page, so no need for a GET method, each time we click the delete button, the function `delete_item` in our flask app will be called, and it'll get as input argument the ID of the item to be deleted (`id=item.id`).

```html
  <td>
    <form action="{{url_for('delete_item', id=item.id)}}" method="post">
      <input type="hidden" name="_method" value="DELETE">
      <input type="submit" value="Delete" class="btn btn-danger">
    </form>
  </td>
```

#### Editing

The editing function in our main flask app will be quite similar to `add_item`. We'll first fetch the item we'll be editing from the database using the ID of the item, this will be passed to the editing page `edit_item.html` so that the current title and task description are displayed in the web-form. 

If we get a POST method, that means that we're sending new data from our web-form, in this case we need to receive the new title and the new task description from the from, create a new database connection, and then update the corresponding field in our table `todolist` with the new information. Finlay, we close the connection and display a success message and redirect the user to the updated `todo` page.

You'll need to the form fields so that we can see the existing information when editing the page (title, task, author), and also get the new variable to send to the database (same functionality as `add_article`).

```python
# Edit Item
@app.route('/edit_item/<string:id>', methods=['GET', 'POST'])
def edit_items(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get an item by id
    result = cur.execute("SELECT * FROM todolist WHERE id = %s", [id])

    item = cur.fetchone()
    cur.close()

    # Get form
    form = ItemForm(request.form)

    # Populate item form the existing item information
    ## ADD YOU CODE HERE 

    if request.method == 'POST' and form.validate():
    	# Get the title / task / author from the passed form
		## ADD YOU CODE HERE

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(title)

        # Execute
        cur.execute ("UPDATE todolist SET title=%s, author=%s, task=%s WHERE id=%s",(title, author, task, id))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Item Updated', 'success')

        return redirect(url_for('todo'))

    return render_template('edit_item.html', form=form)
```

Now create `edit_item.html` which is the same one as `add_items.html`. Maybe try change and add any functionality you'd like to use.

#### Deleting

To delete an a given item, all we need To-Do is create a new route, the same as the one we've declared in `todo.html`. We'll get the item ID as a function argument. Now the next step is to simply create a new connection to the database, execture the correct delete MySQL command, close the connection and redirect the user to the `todo` page. Complete the following function:

```python
# Delete A To-Do list item
@app.route('/delete_item/<string:id>', methods=['POST'])
def delete_item(id):
    # Create cursor, Execute, Commit to DB and Close connection
    # Then redirect the user
```

Now test the edit and delete functionality.

### (Optionnal) Adding a new field for our to-do list

Now let's say we want to add a new field called `done`. See if you can edit our the web-app to add this field, you can also try to add a button in the `todo` page to declare that an item in the `todo` list was accomplished.

### Next

In this tutorial, we've build a website that access our database and displays the To-Do items that are in the database. But what if wanted to take a wider approach, and make the our To-Do list accessible to other developers / clients so that they can add it to their website (our To-Do list is quite important). This can be done using a REST API (well even using plain HTTP, SOAP, or the next kid GraphQL, but we'll focus on REST). Go to the next [tutorial](REST.md).