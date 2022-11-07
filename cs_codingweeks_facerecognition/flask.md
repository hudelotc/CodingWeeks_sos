In this tutorial of the Coding Weeks, we'll build a simple website that will hold some information about your teams, your project, and a To-Do list of the tasks that needs to be accomplished for your project. The web framework of choice is Flask, with some HTML/CSS for the front-end and a MySQL database that we'll hold our To-Do list. We'll first start with an introduction to Flask.

# Introduction to Flask

Flask is a small and powerful web framework for Python. It's easy to learn and simple to use, enabling us to build a web app in a short amount of time.

From the official project page ([Link](https://palletsprojects.com/p/flask/))

> Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

> Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.

## Installing Flask

### Using a virtual environment (recommanded)

During this week, we'll try to use [virtual environments](https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html) that are tailored for our needs and the packages we'll need for a specific project. Generally, where installing packages with `pip` and `sudo apt-get`, these packages are installed globally, which may break some system tools.

By installing them globally, the packages will reside in the default Pyhton path `/usr/lib/python3.7/site-package` (Windows by default in `C:\Users\Your_user_name\AppData\Local\Programs\Python`). So if some packages need a previous version of the python packages for a given project, this action may break it.

To this end, we'll use `virtualenv`. It allows us to avoid installing Python packages globally by making an isolated python environment. That means it will install packages just in the desired project folder.

Let's start by creating a directory where the project will live. Either use the `mkdir folder_name` command if you're using a UNIX system, or `mkdir 'folder_name'` in the windows command line, or simply do it graphically.

```
$ mkdir codingweeks
$ cd codingweeks
```

**Note:** For `anaconda` users, you can skip this part and create a `conda env` instead using anaconda directly (see [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)), and then install Flask.

Now let's create our virtual environment. If you have a Python version older than 3.4, then `virtualenv` is supported natively, all you need to do is run (Note: On Debian/Ubuntu systems, you need to install the python3-venv package using the following command `apt-get install python3-venv` and then replace `python` with `python3`):

```
$ python -m venv codingweeks
```

With this command, we're asking Python to run the `venv` package, which creates a virtual environment named `codingweeks`. The first venv in the command is the name of the Python virtual environment package, and the second is the virtual environment name that we're going to use for this particular environment.

For windows users, type `cmd` in the search bar, and then run the command, if `python` command was not found, the Python path was not added to Windows known paths when it was first installed. So we can either remove Python, and re-install it and this time make sure you choose the option to add it to Path when prompted in the beginning. Or simply add it to the path manually (these two methods are described [here](https://datatofish.com/add-python-to-windows-path/)).

If you're using an earlier version than 3.4. The first step is to install `virtualenv` globally, this will be the only package we'll install this way. So let's run `pip install`, in UNIX run `pip3` instead of `pip`. 

```bash
$ pip install virtualenv
```

And then we'll create our Python virtual environnement.

```bash
$ virtualenv codingweeks
```

In this case, if Python 2 is the default version (Ubuntu), we might end-up with it as our version in the venv (use option `-p python3` in this case).

Regardless of the method we've used to create it, we should have our virtual environment created. Now we have to tell the system that we want to use it, and we do that by activating it. To activate the brand new virtual environment we use the following command:

For UNIX users:

```bash
$ source codingweeks/bin/activate
(venv) $ _
```

For windows user, run the `activate` file in `codingweeks/Scripts/activate`:

```bash
$ codingweeks/Scripts/activate
(venv) $ _
```

Now that we have a virtual environment created and activated, we can finally install Flask in it:

```
(venv) $ pip install flask
```

## The "Hello, World" of Flask

Let's first create our entry file in the project's folder `app.py`. And let's create and run a flask app.

```python
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
```

Run the script and then go to `localhost:5000`, and you'll get a `Not Found` error message. This is because we didn't provide any content for our homepage. To do this we need to create a route. Let's add a simple function that we'll return a string `Hello world` when we access the home page `/`. Add this function after the app creation (`app = Flask(__name__)`) in your script:

```python
# Index
@app.route('/')
def index():
    return "Hello World"
```

Now we need to stop and re-run our app. To enable automatic reloading, we can put our application in debug mode to avoid restarting the application after every modification. To do this, simply replace `app.run()` with `app.run(debug=True)`. When running the script you'll notice a message `Debug mode: on`.


### Constructing the web pages

Normally, we won't return a simple string, but an HTML template when the user is in the home page. To do this we'll use a Flask function called `render_template`, and pass to this function our `.html` template. In our case we'll return an HTML file called `home.html` that's located in `templates/home.html`. First let's import `render_template` and then use it to render `home.html`, this is done as follows:

```python
from flask import Flask, render_template

# Index
@app.route('/')
def index():
    return render_template('home.html')
```

Now let's create the HTML template. First create a `templates` folder, and in it create `home.html`. Now in our file we'll create our HTML page. Normally, each time we want to add a new page, we need to add the same HTML code every time, to avoid this, we can create a layout file, and simple re-use it for each page and then add some functionality that's specific to each page.

So first, create `layout.html` in `templates`. And then add this simple `HTML` layout:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Coding Weeks</title>
  </head>
  <body>
    <div>
      {% block body %}{% endblock %}
    </div>
  </body>
</html>
```

This way, for a given page we'd like to add, we can extend the layout and simply replace `{% block body %}{% endblock %}` with the content of the new page. If we go back to `home.html`, we can add the following:

```html
{% extends 'layout.html' %}

{% block body %}
  <p style="color:#FF0000";> Hello world </p>
{% endblock %}
```

This way, we'll re-use the layout.html and replace `{% block body %}{% endblock %}` with a paragraph tag with the text in red `<p style="color:#FF0000";> Hello world </p>`. This is done based on the Jinja, which in a template engine used with Flask (see [Project page](https://palletsprojects.com/p/jinja/)).

Now go to `localhost:5000`, see if we have the correct output. You can also see the source code of the web page and note how the source code was automatically generated by Flask.

### Adding Bootstrap

Our current design is quite lacking. To have a beautifully designed website. We might use CSS, but getting a beautiful website up and running takes time and efforts. the other option is to use a CSS framework and get things done quickly, while being responsive and beautifully designed. In this project we'll use [bootstrap](https://getbootstrap.com/). What is bootstrap ? Here is the definition from the home page:

> Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. Quickly prototype your ideas or build your entire app with our Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful plugins built on jQuery. 

Adding bootstrap to our website is quite simple, all we need to do is add [BootstrapCDN](https://www.bootstrapcdn.com/) (both CSS and javascript) to our `layout.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Coding Weeks</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  </head>
  <body>

    <div class="container">
      {% block body %}{% endblock %}
    </div>

    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  </body>
</html>
```

If you reload the app, you'll see that the font is different and there the padding too.

Now we'll start using the examples provided ([Bootstrap examples](https://getbootstrap.com/docs/4.3/examples/)). We'll add a navigation bar to our website. First create a folder called `includes` in `templates`, this we'll host all of the 3rd party code we'll use for the website. Then create a new file `_navbar.html`, this file we'll have the code for the navigation bar of our website: 

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light" style="margin-bottom: 20px;">
    <div class="container-fluid">
    <a class="navbar-brand" href="/">Coding Weeks</a>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="/">Home</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/project">Project</a>
          </li>
        <li class="nav-item">
          <a class="nav-link" href="/todo">To-Do</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/about">About</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

You can see that in our navigation bar, we'll have four pages:
- `Home` page referenced by `/`. 
- `About` page containing information about the members of the your group, referenced by `/about`. 
- `Project` page, it gives a simple description of the project, referenced by `/project`. 
- `Todo` page containing a to do list of the things the project member need to accomplish, referenced by `/todo`. 

This is just an example, it is up to you to add the any pages you like. You can also try to use another example of bootstrap [navbar](https://getbootstrap.com/docs/4.3/components/navbar/).

Now we need to include it in our layout. 

```html
  ....
  <body>
    {% include 'includes/_navbar.html' %}
  ....
```

In the HTML layout, we see that our `block` is not enclosed in any HTML tag. Let's enclose it in a [container](https://getbootstrap.com/docs/4.0/layout/overview/), this way we can control it's placement in the page, the paddings, ect. Try it with other options and see the difference (e.g. `container-fluid`)

```html
  ....
    <div class="container">
        {% include 'includes/_messages.html' %}
        {% block body %}{% endblock %}
    </div>
  ....
```

You'll notice that we've also included a new file, `includes/_messages.html` will contain the block of code that will display warning / notification messages when we pass them to the `render_template` function as arguments. If the passed argument if an error we'll display it in red (`danger`), if not it'll be displayed in green (`success`). The HTML code of `includes/_messages.html`:

```html
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    {% for category, message in messages %}
      <div class="alert alert-{{ category }}">{{ message }}</div>
    {% endfor %}
  {% endif %}
{% endwith %}

{% if error %}
  <div class="alert alert-danger">{{error}}</div>
{% endif %}

{% if msg %}
  <div class="alert alert-success">{{msg}}</div>
{% endif %}
```

For our home page, we can use another bootstrap example, let's replace `Hello world` with a `Jumbotron` element (see [details](https://getbootstrap.com/docs/4.0/components/jumbotron/)):

```html
  <div class="jumbotron text-center">
    <h1>Welcome to our Coding Weeks project webpage</h1>
    <p class="lead">This application is built on the Python Flask framework and is the focus of the "Coding Weeks" course</p>
  </div>
```

Go to the app page and see the resutls.

### Adding the rest of the pages

Until now, we've created our nav bar with four pages, but only the home page is functional, this is because we only have one route added in the `app.py` file. Now you'll need to create the rest of the routes and their corresponding HTML files.

For example, for the `About page`, we first create a route:

```python
# About
@app.route('/about')
def about():
    return render_template('about.html')
```

And then in `templates`, we create the HTML file `about.html`:

```html
{% extends 'layout.html' %}

{% block body %}
  <h1>About Us</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
{% endblock %}
```

Do the same thing for the `Project` page. You can use some simple [HTML examples](https://www.w3schools.com/html/html_examples.asp) or [Bootstrap examples](https://getbootstrap.com/docs/4.0/examples/).

### To do list
For the to do list page, we'd like to load the to do list from a given data source, and then loop though all the elements and add them to our webpage. So first let's create a data source, a simple python function that we'll give us the element of a To Do list when it's called. In the project folder, let's create `data.py` and in it, let's create a function called `get_todo()`.

```python
def GetTodoList():
    todo_list = [
        {
            'id': 1,
            'title':'Create Flask APP',
            'task':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'author':'Name',
            'create_date':'11-11-2019'
        },
        {
            'id': 2,
            'title':'Add Bootstrap',
            'task':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat',
            'author':'Name',
            'create_date':'11-11-2019'
        },
        {
            'id': 3,
            'title':'Create Routes',
            'task':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat',
            'author':'Name',
            'create_date':'11-11-2019'
        },
        {
            'id': 4,
            'title':'File for an IPO',
            'task':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat',
            'author':'Name',
            'create_date':'11-11-2019'
        }
    ]
    return todo_list
```

The next step is to create a route, this time we also need to pass the data to our HTML template, the data is imported from the python file we've created and passed as an argument to the rendering function:

```python
# Get data
from data import GetTodoList
todo_list = GetTodoList()

# Todo list
@app.route('/todo')
def todo():
    return render_template('todo.html', todo_list=todo_list)
```

Now we go templates and create a new HTML file, in it we'll loop through the element of the To-Do list we've passed, this can be done using the [Jinja](https://palletsprojects.com/p/jinja/) template iterator `{% for i in list %}`. Note how we loop through the variable `todo_list` passed from the Flaks app:

```html
{% extends 'layout.html' %}

{% block body %}
  <h1>To Do list</h1>
  <ul class="list-group">
    {% for element in todo_list %}
      <li class="list-group-item">
        <a href="todo/{{element.id}}">{{element.title}}</a>
      </li>
    {% endfor %}
  </ul>
{% endblock %}
```

Above, we're using a bootstrap class `list-group` inside an unordered list tag (`<ul>`), and each element in added inside `<li>` tage with a bootstrap class `list-group-item`. We wrap each element with a link, beacuse we want each element in the to do list to have its unique webpage referenced by the `id` of the element.

Now we need to create the routes for each element in the to do list, we can't do this manually for each element. In this case we need to create routes dynamically:

```python
@app.route('/todo/<string:id>/')
def items(id):
    return render_template('items.html', id=id)
```

And we'll create the html `items.html` file, and for now, let's just display the ID:

```html
{% extends 'layout.html' %}

{% block body %}
  <h1>{{id}}</h1>
{% endblock %}
```

Now go to the webpage, and try `localhost:5000/todo/100/` or any ID, and you'll see the given ID displayed.

## Next
Storing the To-Do list in an MySQL database and connecting it to our Flask app. [Go to the next tutorial](database.md).