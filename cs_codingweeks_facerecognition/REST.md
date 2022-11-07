# RESTful API with Python and Flask

In recent years REST (REpresentational State Transfer) has emerged as the standard architectural design for web services and web APIs. In this tutorial we're going to create a RESTful web service using Python and Flask to access our To-Do list.

### What is REST?

<p align="center"><img src="Images/restAPI.png" align="center" width="400"></p>

The characteristics of a REST system are defined by six design rules:
- Client-Server: There should be a separation between the server that offers a service, and the client that consumes it.
- Stateless: Each request from a client must contain all the information required by the server to carry out the request. In other words, the server cannot store information provided by the client in one request and use it in another request.
- Cacheable: The server must indicate to the client if requests can be cached or not.
- Layered System: Communication between a client and a server should be standardized in such a way that allows intermediaries to respond to requests instead of the end server, without the client having to do anything different.
- Uniform Interface: The method of communication between a client and a server must be uniform.
- Code on demand: Servers can provide executable code or scripts for clients to execute in their context. This constraint is the only one that is optional.

### What is a RESTful web service?

The REST architecture was originally designed to fit the HTTP protocol that the world wide web uses.

Central to the concept of RESTful web services is the notion of resources. Resources are represented by [URIs](https://fr.wikipedia.org/wiki/Uniform_Resource_Identifier). The clients send requests to these URIs using the methods defined by the HTTP protocol, and possibly as a result of that the state of the affected resource changes.

The HTTP request methods are typically designed to affect a given resource in standard ways:


| HTTP Method           | Action                              |
| ----------------------|:-----------------------------------:|
| GET                   | Obtain information about a resource |
| POST                  | Create a new resource               |
| PUT                   | Update a resource                   |
| DELETE                | Delete a resource                   |


### Designing a simple web service

The task of designing a web service or API that adheres to the REST guidelines then becomes an exercise in identifying the resources that will be exposed and how they will be affected by the different request methods.

Let's say we want to write a our To-Do list application as a REST API and design a web service for it. The first thing to do is to decide what is the root URL to access this service. For example, we could expose this service as:

```
http://[hostname]/todo/api/v1.0/
```

Here we include the name of the application and the version of the API in the URL. Including the application name in the URL is useful to provide a `namespace` that separates this service from others that can be running on the same system. Including the version in the URL can help with making updates in the future, since new and potentially incompatible functions can be added under a new version, without affecting applications that rely on the older functions.

Our tasks resource will use HTTP methods as follows:

| HTTP Method           | Action                                            | Action                    |
| ----------------------|:-------------------------------------------------:|:-------------------------:|
| GET                   | `http://[hostname]/todo/api/v1.0/items`           | Retrieve list of items    |
| GET                   | `http://[hostname]/todo/api/v1.0/items/[item_id]` | Retrieve an item          |
| POST                  | `http://[hostname]/todo/api/v1.0/items`           | Create a new To-Do item   |
| PUT                   | `http://[hostname]/todo/api/v1.0/items/[item_id]` | Update an existing item   |
| DELETE                | `http://[hostname]/todo/api/v1.0/items/[item_id]` | Delete an item            |


Just like the web-page, we can define a task or a To-Do list item as having the following fields:

- `id`: unique identifier for the items. Numeric type.
- `author`: The name of the creator of the task to be done. String type.
- `title`: short task description. String type.
- `task`: long task description. Text type.
- `done`: task completion state. Boolean type.

And with this we are basically done with the design part of our web service, now let's implement it.

### Implementing RESTful services in Python and Flask

Building web services with Flask is surprisingly simple. There are a couple of Flask extensions that help with building RESTful services with Flask, but the task in hand is quite simple, so no need to use an extension.

The clients of our web service will be asking the service to add, remove and modify an given to-do item, so clearly we need to have a way to store items. Just like our web-site, first we used a simple python script to store the items, then a MySQL database. So this we'll also start with just a plain python script, and it is up to you to use what we've learned in the last tutorial to adjust the presented approach to use a MySQL database, and then create, edit and delete items from it.

Just like last time, our `data.py` file will look like this:

```python
def GetTodoList():
    todo_list = [
        {
            'id': 1,
            'title': 'Design the API',
            'task': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 
            'author':'Name',
            'done': False
        },
        {
            'id': 2,
            'title': 'Create a simple memory file',
            'task': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 
            'author':'Name',
            'done': False
        },
        {
            'id': 3,
            'title': 'Implement the API',
            'task': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 
            'author':'Name',
            'done': False
        },
        {
            'id': 4,
            'title': 'Profit',
            'task': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 
            'author':'Name',
            'done': False
        }
    ]
    return todo_list
```

And similar to the website, let's launch a bare-bones Flask app in `rest_api.py`:

```python
from data import GetTodoList
from flask import Flask, jsonify


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
```


### GET method

Using the base Flask app we are now ready to implement the first entry point of our web service:

```python
items = GetTodoList()

@app.route('/todo/api/v1.0/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})
```

As you can see, we created a dictionary that we'll simulate a database of To-Do tasks, which is nothing more than a plain and simple array of dictionaries. Each entry in the array has the fields that we defined above for our tasks. With a `get_items` function that is associated with the `/todo/api/v1.0/items` URI, and only for the `GET` HTTP method.

The response of this function is not text, we are now replying with JSON data, which Flask's jsonify function generates for us from our data structure.

Using a web browser to test a web service isn't the best idea since web browsers cannot easily generate all types of HTTP requests. Instead, we will use cURL.

#### cURL

For UNIX users, simply run `apt-get install curl`, for Windows users:

- If you are on Windows 10, version 1803 or later, your OS ships with a copy of curl, already set up and ready to use.

- If you have Git for Windows installed (can be downloaded `from git-scm.com`), you have curl.exe under: `C:\Program Files\Git\mingw64\bin\`. Simply add the above path to PATH.

- In not, you can simply download the following [package](https://curl.haxx.se/download.html), just unzip it wherever you want. No need to install.


Now, let's go back to our API, and let's start the web service by running `rest_api.py`. Then in a new console window and we'll run the following command:

```bash
$ curl -i http://localhost:5000/todo/api/v1.0/items`
```

You'll need to get `HTTP/1.0 200 OK` message, with the rest of the HTTP headers, and the todo list content. Take you time to understand each field.

Now let's write the second version of the `GET` method for our To-Do list items. If you look at the table above this will be the one that is used to return the data of a single item:

```python
from flask import abort

@app.route('/todo/api/v1.0/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        abort(404)
    return jsonify({'item': item[0]})
```

This second function is a little bit more interesting. Here we get the `id` of the item in the URL, and Flask translates it into the `item_id` argument that we receive in the function. With this argument we search our items array. If the `id` that we were given does not exist in our database then we return the familiar error code 404, which according to the HTTP specification means "Resource Not Found", which is exactly our case.

If we find the item then we just package it as JSON with jsonify and send it as a response, just like we did before for the entire collection. Here is how this function looks when invoked with curl:

```bash
$ curl -i http://localhost:5000/todo/api/v1.0/items/2
```

Check if you get the correct response, now try to fetch a non existing item.

As you may have noticed, when requesting an non existing item, we got an HTML message instead of JSON, because that is how Flask generates the 404 response by default. Since this is a web service client applications will expect that we always respond with JSON, so we need to improve our 404 error handler:

```python
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
```

Now see if the we get a clearer error message this time around.

### POST method

Next in our list is the POST method, which we will use to insert a new item in our items database:

```python
from flask import request

@app.route('/todo/api/v1.0/items', methods=['POST'])
def create_item():
    if not request.json or not 'title' in request.json:
        abort(400)
    item = {
        'id': items[-1]['id'] + 1,
        'title': request.json['title'],
        'task': request.json.get('task', ""),
        'done': False
    }
    items.append(item)
    return jsonify({'item': item}), 201
```

Adding a new item is also pretty easy. The `request.json` will have the request data, but only if it came marked as JSON. If the data isn't there, or if it is there, but we are missing a title item then we return an error code 400, which is the code for the bad request.

We then create a new item dictionary, using the ID of the last item plus one (a cheap way to guarantee unique ids in our simple database). We tolerate a missing task description field, and we assume the done field will always start set to False.

We append the new item to our items array, and then respond to the client with the added item and send back a status code 201, which HTTP defines as the code for "Created".

To test this new function we can use the following curl command:

```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Use a MySQL database"}' http://localhost:5000/todo/api/v1.0/items
```

If you are on Windows, under normal circumenstances, the above command should work just fine. However,
for some the native versions of curl, you can get an error. If that is the case you'll need to send double quotes inside the body of a request:

```bash
$ curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Use a MySQL database"""}" http://localhost:5000/todo/api/v1.0/items
```

Make sure the API is functional by making a combination of POST and GET calls and see if the results are correct.

### PUT method

With a put method, we'll update an existing item, we'll write a simple `update_item` function. Before updating an existing item, and to prevent bugs, we need to do an exhaustive checking of the input arguments. We need to make sure that anything that the client provided us is in the expected format before we incorporate it into our database.

```python
@app.route('/todo/api/v1.0/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'task' in request.json and type(request.json['task']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    item[0]['title'] = request.json.get('title', item[0]['title'])
    item[0]['task'] = request.json.get('task', item[0]['task'])
    item[0]['done'] = request.json.get('done', item[0]['done'])
    return jsonify({'item': item[0]})
```

Now let's update the item #2 as being done:

```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/items/2
```

### DELETE method

Now, based on the examples above, try to implement a DELETE method using a flask route function, and test it using curl.

### Improving the web service interface

The problem with the current design of the API is that clients are forced to construct URIs from the task identifiers that are returned. This is pretty easy in itself, but it indirectly forces clients to know how these URIs need to be built, and this will prevent us from making changes to URIs in the future.

Instead of returning item IDs we can return the full URI that controls the item, so that clients get the URIs ready to be used. For this we can write a small helper function that generates a "public" version of a task to send to the client:

```python
from flask import url_for

def make_public_item(item):
    new_item = {}
    for field in item:
        if field == 'id':
            new_item['uri'] = url_for('get_item', item_id=item['id'], _external=True)
        else:
            new_item[field] = item[field]
    return new_item
```

All we are doing here is taking an item from our database and creating a new item that has all the fields except ID, which gets replaced with another field called `uri`, generated with Flask's `url_for`. 

Use this helper function when we call the GET methods to retrieve all the tasks. Run the cURL command and make sure we get the URIs in the place of the item IDs.

### Securing the web service

Our current web serve is open to all user, but if a stranger figures out how our API works he or she can write a new client that can access our service and mess with our data.

The easiest way to secure our web service is to require clients to provide a user-name and a password. In a regular web application you would have a login form that posts the credentials, and at that point the server would create a session for the logged in user to continue working, with the session ID stored in a cookie in the client browser. Unfortunately doing that here would violate the stateless requirement of REST, so instead we have to ask clients to send their authentication information with every request they send to us.

Let's try using one of the Flask extensions `Flask-HTTPAuth` and setup a very simple authentication that only accepts a number of predefined passwords and user-names. First let's install the package in our virtualenv:

```bash
pip install flask-httpauth
```

Let's say we want our web service to only be accessible to username `codingweeks` and password `python`. We can setup a Basic HTTP authentication as follows:

```python
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'codingweeks':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
```

The `get_password` function is a callback function that the extension will use to obtain the password for a given user. In a more complex system this function could check a user database, but in this case we just have a single user so there is no need for that.

The `error_handler` callback will be used by the extension when it needs to send the unauthorized error code back to the client. Like we did with other error codes, here we customize the response so that is contains JSON instead of HTML.

With the authentication system setup, all that is left is to indicate which functions need to be protected, by adding the `@auth.login_required` decorator. Add this decorator for the `get_items` function. And the call cURL and see if you get the correct error message (`"error": "Unauthorized access"`).

Now try to send the user authentication info using the cURL option `-u user:password` with a GET call, and see if now you are able retrieve all the of To-Do list items.

### Optional: Using a database

Base on the web-page we've created in the previous tutorial. Try to can create a new database / table (or reuse the old one, up to you) that will hold the To-Do list items in a given table, and with each method call (GET, POST, ...), create a new connection to the database, apply the correct MySQL commands to / fetch transform the data in the correct way.

### Next
Your turn.